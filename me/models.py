from django.db import models

class Skill(models.Model):
    LEVEL_CHOICES = [(i, f"{i}%") for i in range(0, 101, 10)]

    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES, default=50)

    def __str__(self):
        return f"{self.name} ({self.level}%)"

class Project(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=10000)
    description = models.TextField()
    visit_link = models.URLField(max_length=10000)
    tech_stack=models.CharField(max_length=100,null=True, blank=True)


    def __str__(self):
        return self.title
class ProfessionalSkill(models.Model):
    LEVEL_CHOICES = [(i, f"{i}%") for i in range(0, 101, 10)]

    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES, default=50)

    def __str__(self):
        return f"{self.name} ({self.level}%)"
class Hobby(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
class Certificates(models.Model):
    name=models.CharField(max_length=1000)
    issued_by=models.CharField(max_length=1000)
    issued_date=models.DateField()
    img = models.CharField(max_length=1000, null=True, blank=True)

    note=models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return f"{self.name}"
    
