from django.urls import path
from . import views

app_name = "ije"

urlpatterns = [
	path('', views.index , name="index"),
	path('journal-info/peer-review-process/', views.prp, name="prp"),
	path('journal-info/about-journal/', views.aj, name="aj"),
	path('journal-info/publication-ethics/', views.pe, name="pe"),
	path('guide-for-authors/', views.gfa, name="gfa"),
	path('reviewers/', views.review, name="review"),
	path('login/', views.login , name="login"),
]