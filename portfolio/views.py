from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def home(request):
  return render(request,"portfolio/home.html")

def about(request):
  return render(request,"portfolio/about.html")

def projects(request):
  return render(request,"portfolio/projects.html")

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contactus.html', {'form': form})

