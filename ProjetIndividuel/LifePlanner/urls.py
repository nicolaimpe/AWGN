from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projets_liste'),
    path('project/<int:id_project>', views.project, name = 'taches_liste')
]
