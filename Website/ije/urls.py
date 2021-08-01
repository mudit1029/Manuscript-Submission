from django.urls import path
from . import views

app_name = "ije"

urlpatterns = [
	path('', views.index , name="index"),
	path('contact-us/', views.contact , name="contact"),
	path('journal-info/peer-review-process/', views.prp, name="prp"),
	path('journal-info/about-journal/', views.aj, name="aj"),
	path('journal-info/publication-ethics/', views.pe, name="pe"),
	path('guide-for-authors/', views.gfa, name="gfa"),
	path('reviewers/', views.review, name="review"),
	path('advisory-editorial-board/', views.aeb, name="aeb"),
	path('editorial-board/', views.eb, name="eb"),
	path('login/', views.signIn , name="login"),
	path('submit-manuscript/', views.submit_manuscript , name="submit_manuscript"),
	path('details/', views.details , name="details"),
	path('logout/', views.signout , name="signout"),
]