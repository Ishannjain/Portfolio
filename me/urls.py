from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path('projects/', views.projects_view, name='projects'),
    path('about/', views.about_view, name='about'),

]