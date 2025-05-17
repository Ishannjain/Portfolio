from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from .models import *

def index(request):
    return render(request,"me/layout.html")

def projects_view(request):
    projects = Project.objects.all()
    skills = Skill.objects.prefetch_related('project_set')
    hobbies=Hobby.objects.all()
    Certificatess=Certificates.objects.all()
    return render(request, 'me/projects.html', {
        'projects': projects,
        'skills':skills,
        'hobbies':hobbies,
        'Certificatess': Certificatess
        })
def about_view(request):
    ProfessionalSkills = ProfessionalSkill.objects.all()
    hobbies = Hobby.objects.all()
    return render(request, 'me/about.html', {
        'skills': ProfessionalSkills,
        'hobbies': hobbies
    })
