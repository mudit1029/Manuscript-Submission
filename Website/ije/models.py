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
	user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "author")
	title =  models.CharField(max_length=64)	
	article_type =  models.CharField(max_length=64)
	special_title =  models.CharField(max_length=64)
	classification =  models.CharField(max_length=64)
	abstract =  models.CharField(max_length=120)
	keywords =  models.CharField(max_length=120)

	def __str__(self):
		return (f"{self.user} :- {self.title}")
