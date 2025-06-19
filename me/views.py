from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from .models import *

def index(request):
    known=known_things.objects.all()
    topprojs=topproj.objects.all()
    Timelines=Timeline.objects.all()
    skills=Skill.objects.all()
    pro=ProfessionalSkill.objects.all()
    return render(request,"me/index.html",{
        'skills':skills,
        'pro':pro,
        'times':Timelines,
        'topprojs':topprojs,
        'known':known
    })

def projects_view(request):
    topprojs=topproj.objects.all()
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
        'Certificatess': Certificatess,
        'topprojs':topprojs
        })
def about_view(request):
    more=more_about.objects.all()
    ProfessionalSkills = ProfessionalSkill.objects.all()
    hobbies = Hobby.objects.all()
    return render(request, 'me/about.html', {
        'proskills': ProfessionalSkills,
        'hobbies': hobbies,
        'more':more
    })
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'me/detail_proj.html', {
        'project': project
    })
def cert_detail(request, id):
    cert = get_object_or_404(Certificates, id=id)
    return render(request, 'me/cert_detail.html', {
        'cert':cert
    })
def detail_hobby(request, id):
    hob = get_object_or_404(Hobby, id=id)
    return render(request, 'me/detail_hobby.html', {
        'hob':hob
    })
