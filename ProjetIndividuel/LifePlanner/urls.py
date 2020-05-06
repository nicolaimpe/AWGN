"""LifePlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page : list of the projects of the current user
    path('projects/', views.projects, name='projets_liste'),
    # Second page : list of the tasks associated with the project characterized by id = id_project
    path('project/<int:id_project>/', views.project, name='taches_liste'),
    # Third page : Visualization of the task characterized by id = id_project, its attributes and the associated journal
    path('task/<int:id_task>/', views.task, name='affichage_tache'),
    # Page for the creation of a new task by means of a form
    path('project/<int:id_project>/newtask/', views.create_task, name='creation_tache'),
    # Page for the modification of the task the user is visualizeing  by means of the same form as for the creation but already filled with the existing data (which are supposed to be modified)
    path('project/<int:id_project>/edittask/<int:id_task>/', views.edit_task, name='modification_tache')
]
