from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from .models import *

def index(request):
    skills=Skill.objects.all()
    pro=ProfessionalSkill.objects.all()
    return render(request,"me/index.html",{
        'skills':skills,
        'pro':pro
    })

def projects_view(request):
    projects = Project.objects.all()
    skills = Skill.objects.prefetch_related('project_set')
    hobbies=Hobby.objects.all()
    Certificatess=Certificates.objects.all()
    ProfessionalSkills = ProfessionalSkill.objects.all()
    return render(request, 'me/projects.html', {
       'proskills': ProfessionalSkills,
        'projects': projects,
        'skills':skills,
        'hobbies':hobbies,
        'Certificatess': Certificatess
        })
def about_view(request):
    ProfessionalSkills = ProfessionalSkill.objects.all()
    hobbies = Hobby.objects.all()
    return render(request, 'me/about.html', {
        'proskills': ProfessionalSkills,
        'hobbies': hobbies
    })
