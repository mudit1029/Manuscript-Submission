from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser , Manuscript
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login , logout , authenticate
# Create your views here.
def index(request):
	return render(request, "ije/index.html")

def contact(request):
	return render(request, "ije/contact.html")

def prp(request):
	data = "Once a paper is submitted online, editor in the related field as an expert should check the paper. After primary screening the paper send to reviewers. The reviewer respond has to be presented to Editorial board meeting for further evaluation. From the review process and editorial board evaluation we decide for revision or reject. In the case of a paper Editorial board is unable to judge the given comments by the reviewer and the revised paper. As author is asked for revision, the whole folder send to final referee for the exact judgment. Author at revision stage must prepare rebuttal letter for respond to itemized comments given by reviewer. Editorial board based on complete cycle of revision if the revision is satisfied may vote for acceptance."	
	return render(request, "ije/index.html" ,{
		"prp": data
		})

def aj(request):
	return render(request, "ije/aj.html")

def pe(request):
	return render(request, "ije/pe.html")

def gfa(request):
	gfa = "1"
	return render(request, 'ije/aj.html', {
		'gfa': gfa
		})

def review(request):
	review = "1"
	return render(request, 'ije/index.html', {
		'review': review
		})				

def signIn(request):
	if request.method == "POST":

		#Get all the data posted by the user.
		email = request.POST["email"]
		password = request.POST["password"]

		#Set the username field to the user provided username.
		kwargs = {'email':email}	

		# try to get the user by the user data.	
		try :	
			user = CustomUser.objects.get(**kwargs)

		# if the user does not exist in the database	
		except CustomUser.DoesNotExist:

			# Return the login page again with the provided data and with a message says "User Does Not Exist".
			return render(request, "ije/login.html",{
				"message": "Email Is Incorrect"
			})

		"""# If the user activity status is false			
		if user.is_active == False :

			#return the register page With the below message and with an registeration form.
			return render(request, "users/register.html",{
				"message": "Account Error : Re-Register with the same credentials.",
				"form": RegisterForm(),
				"button": "Register"
				})	"""

		# If the user provided password match the user password in the database					
		if user.check_password(password):

			# Grant login to the user
			login(request, user)

		# Otherwise if the password did'nt match	
		else :

			#Return login page again with a message "Invalid Credentials"
			return render(request, "ije/login.html",{
			"message": "Password Is Incorrect",
			"email": email
			})

		# When user set to login return the user to the index page of movies app.		
		return HttpResponseRedirect(reverse("ije:details"))

	# Open login page when the user method = GET.			
	return render(request, "ije/login.html")	

def submit_manuscript(request):
	if request.method == 'POST' :
		if not request.user.is_authenticated :
			fname = request.POST["fname"]
			lname = request.POST["lname"]
			email = request.POST["email"]
			a_email = request.POST["a_email"]
			number = request.POST["number"]
			region = request.POST["region"]
			title = request.POST["title"]
			typee = request.POST["type"]
			stitle = request.POST["stitle"]
			classification = request.POST["classification"]
			abstract = request.POST["abstract"]
			keywords = request.POST["keywords"]


			password = request.POST["password"]
			confirm = request.POST["confirm"]
			if password != confirm :
				return render(request, "ije/submit_manuscript.html", {
					"fname": fname,
					"lname": lname,
					"email": email,
					"a_email": a_email,
					"number": number,
					"region": region,
					"title": title,
					"typee": typee,
					"stitle": stitle,
					"classification": classification,
					"password": "(Password Did Not Match)",
					"confirm": "(Password Did Not Match)",
					"file": "(Please Attach Your File Again)",
					})


			user = CustomUser.objects.create_user(email,email,password)
			user.first_name = fname
			user.last_name = lname
			user.alternate_email = a_email
			user.number = number
			user.region = region
			user.save()

			file = request.FILES["file"]
			fs = FileSystemStorage()
			file = fs.save(file.name, file)
			fileurl = fs.url(file)
			data = Manuscript(user=user , title=title , article_type = typee , special_title=stitle , classification=classification , abstract=abstract , keywords=keywords , file="/static/uploads"+fileurl)
			data.save()
			login(request, user)
			return HttpResponseRedirect(reverse("ije:details"))

		title = request.POST["title"]
		typee = request.POST["type"]
		stitle = request.POST["stitle"]
		classification = request.POST["classification"]
		abstract = request.POST["abstract"]
		keywords = request.POST["keywords"]	

		file = request.FILES["file"]
		fs = FileSystemStorage()
		file = fs.save(file.name, file)
		fileurl = fs.url(file)
		data = Manuscript(user=request.user , title=title , article_type = typee , special_title=stitle , classification=classification , abstract=abstract , keywords=keywords , file="/static/uploads"+fileurl)
		data.save()
		return HttpResponseRedirect(reverse("ije:details"))
	return render(request, "ije/submit_manuscript.html")

def details(request):
	if not request.user.is_authenticated :
		return HttpResponseRedirect(reverse("ije:index"))
	user = request.user
	data = Manuscript.objects.all().filter(user=user)
	return render(request, "ije/details.html", {
		"data": data
		})

def signout(request):
	logout(request)
	return HttpResponseRedirect(reverse("ije:index"))	