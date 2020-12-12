from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
	context = {
	   'posts': Post.objects.all()
	}
	return render(request, 'blog/index.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'about'})

def skills(request):
	return render(request, 'blog/skills.html', {'title':'skills'})

def contact(request):
	return render(request, 'blog/contact.html', {'title':'contact'})

def project(request):
	return render(request, 'blog/project.html', {'title':'project'})