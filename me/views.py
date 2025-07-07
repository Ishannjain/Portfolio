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

from django.shortcuts import render
from .models import Project, Skill, Hobby, Certificates, ProfessionalSkill, topproj

def projects_view(request):
    topprojs = topproj.objects.all()
    all_projects = Project.objects.all()
    skills = Skill.objects.prefetch_related('project_set')
    hobbies = Hobby.objects.all()
    certificates = Certificates.objects.all()
    professional_skills = ProfessionalSkill.objects.all()

    grouped_skills = []
    other_projects = []

    for skill in skills:
        skill_projects = skill.project_set.all()
        if skill_projects.count() >= 3:
            grouped_skills.append({
                'skill': skill,
                'projects': skill_projects
            })
        else:
            other_projects.extend(skill_projects)

    return render(request, 'me/projects.html', {
        'proskills': professional_skills,
        'skills': skills,
        'hobbies': hobbies,
        'Certificatess': certificates,
        'topprojs': topprojs,
        'grouped_skills': grouped_skills,      # NEW: for skills with 3+ projects
        'other_projects': other_projects       # NEW: merged category
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
