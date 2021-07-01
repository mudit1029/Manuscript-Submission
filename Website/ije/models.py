from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
	email = models.EmailField(unique=True)
	alternate_email = models.EmailField(null=True)
	number = models.IntegerField(null=True)
	region = models.CharField(max_length=64, null=True)

	def __str__(self):
		return (f"{self.id} : {self.first_name} {self.last_name}")

class Manuscript(models.Model):

	Choices = (('SUBMITTED', 'SUBMITTED'),('IN PROCESSING', 'IN PROCESSING'),('SUCCESSFUL', 'SUCCESSFUL '),('FAILED', 'FAILED'))

	user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "author")
	title =  models.CharField(max_length=64)	
	article_type =  models.CharField(max_length=64)
	special_title =  models.CharField(max_length=64)
	classification =  models.CharField(max_length=64)
	abstract =  models.TextField()
	keywords =  models.TextField()
	file = models.URLField(max_length=200 , default="www.google.com")
	status = models.CharField(max_length=20, choices=Choices, default='SUBMITTED') 
	def __str__(self):
		return (f"{self.user} :- {self.title}")
