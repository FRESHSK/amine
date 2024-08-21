from django.urls import path
from . import views
urlpatterns = [
  path("home/",views.home, name="home"), #home page
  path("about/", views.about, name="about"),
  path("projects/", views.projects, name="projects"),
  path('contactus/', views.contactus, name="contact"),
  
]