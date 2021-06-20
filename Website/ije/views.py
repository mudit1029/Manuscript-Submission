from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, "ije/index.html")

def prp(request):
	data = "Once a paper is submitted online, editor in the related field as an expert should check the paper. After primary screening the paper send to reviewers. The reviewer respond has to be presented to Editorial board meeting for further evaluation. From the review process and editorial board evaluation we decide for revision or reject. In the case of a paper Editorial board is unable to judge the given comments by the reviewer and the revised paper. As author is asked for revision, the whole folder send to final referee for the exact judgment. Author at revision stage must prepare rebuttal letter for respond to itemized comments given by reviewer. Editorial board based on complete cycle of revision if the revision is satisfied may vote for acceptance."	
	return render(request, "ije/index.html" ,{
		"prp": data
		})

def aj(request):
	return render(request, "ije/aj.html")

def pe(request):
	return render(request, "ije/pe.html")	