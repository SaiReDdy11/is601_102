from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'home.html', {'name': 'Your Name', 'photo_url': 'https://example.com/photo.jpg', 'email': 'your.email@example.com', 'github': 'https://github.com/SaiReDdy11/is601_102.git'})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def about(request):
    return render(request, 'about.html', {'bio': 'Hello, This is Sai Kumar Reddy,  Enthusiastic engineering graduate with basic knowledge in coding and design. Proficient in C++, HTML 5, JavaScript, and Python. Ability to learn new softwares and technologies quickly. Capability to work in teams by providing valuable support.'})





