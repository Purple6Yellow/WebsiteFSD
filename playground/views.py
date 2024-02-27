from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView


def say_hallo1 (request):
    return HttpResponse('Hello World')

# Opmerking in Python is #

# render wordt gebruikt voor html bestanden

def say_hallo2(request):
    return render(request, 'hello.html', {'name': 'Violette'})

def Agenda (request):
    return render (request, 'blog/Agenda.html', {})

def Blog (request):
    return render (request, 'blog/Blog.html', {})


##
def home_index (request):
    return render (request, 'Index.html', {})

def Overons (request):
    return render (request, 'Overons.html', {})

def Tarieven (request):
    return render (request, 'Tarieven.html', {})

def Contact (request):
    return render (request, 'Contact.html', {})

def BlogJava (request):
    return render (request, 'BlogJava.html', {})

def Blog5 (request):
    return render (request, 'Blog5.html', {})

def Blogdetail (request):
    return render (request, 'Blogdetail.html', {})

def BlogInvullen (request):
    return render (request, 'BlogInvullen.html', {})