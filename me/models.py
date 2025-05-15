from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    image_url = models.URLField(max_length=10000)
    description = models.TextField()
    visit_link = models.URLField(max_length=10000)

    def __str__(self):
        return self.title
