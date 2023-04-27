# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProjectForm
from .models import Project


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


@login_required
def addproject(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectForm()

    context = {
        'form': form
    }
    return render(request, 'project_create.html', context)


@login_required
def home(request):
    return render(request, 'home.html',
                  {'name': 'Sai Kumar Reddy', 'photo_url': 'https://example.com/photo.jpg',
                   'email': 'Chinthakuntaasaikumarreddy@gmail.com',
                   'github': 'https://github.com/SaiReDdy11'})


@login_required
def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})


@login_required
def about(request):
    return render(request, 'about.html', {
        'bio': 'Hello, I am Sai Kumar Reddy, a skilled professional in the field of Computer Science and Engineering. I have completed various projects related to Cyber Cafe, Data Stream, and Edutech Pro, showcasing my diverse experience and ability to work on different projects. I possess strong technical skills in HTML, CSS, JavaScript, Bootstrap, and React, indicating my expertise in web development and front-end technologies. Additionally, my behavior skills such as being an innovator, problem solver, and technology enthusiast make me a valuable asset in any technical team. My willingness to take on new challenges and keep up with the latest trends and advancements in the field makes me a versatile professional. I am always eager to learn and enhance my skills and knowledge to stay at the forefront of the industry. Overall, I am a skilled and passionate professional with a background in technology, possessing diverse experience and expertise. My personality traits such as being an innovator and problem solver make me a valuable asset in any technical team.'})


def logout_view(request):
    logout(request)
    return redirect('login')
