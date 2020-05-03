from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, Task, Status

from .forms import  ConnexionForm
#from .models import Article, Contact

# Create your views here.

@login_required()
def projects(request):
    user = request.user
    projects = user.project_set.all()
    return render(request, 'LifePlanner/projects.html', locals())

@login_required()
def project(request,id_project):
    user = request.user
    project = get_object_or_404(Project,id = id_project)
    tasks = project.task_set.all()
    return render(request, 'LifePlanner/project.html', locals())