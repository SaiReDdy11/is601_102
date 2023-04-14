from django.shortcuts import render
from django.shortcuts import render
from .models import Project
def home(request):
    return render(request, 'home.html')
def portfolio(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio.html', context)
def about(request):
    return render(request, 'about.html')


# Create your views here.
