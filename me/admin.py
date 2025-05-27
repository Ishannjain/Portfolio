from django.contrib import admin
from .models import *
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

admin.site.register(Project)
admin.site.register(Certificates)
admin.site.register(Hobby)
admin.site.register(Timeline)
@admin.register(ProfessionalSkill)
class ProfessionalSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')