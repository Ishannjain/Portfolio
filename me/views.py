from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from .models import *

def index(request):
    return render(request,"me/layout.html")

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'me/projects.html', {'projects': projects})
def skills_view(request):
    skills= Skill.objects.all()
    return render(request, 'me/skills.html', {'skills':skills})