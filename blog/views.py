from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'blog/index.html')

def about(request):
	return render(request, 'blog/about.html', {'title':'about'})

def skills(request):
	return render(request, 'blog/skills.html', {'title':'skills'})

def contact(request):
	return render(request, 'blog/contact.html', {'title':'contact'})

def project(request):
	return render(request, 'blog/project.html', {'title':'project'})