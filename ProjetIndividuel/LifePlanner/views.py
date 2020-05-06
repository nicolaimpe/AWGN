"""LifePlanner views definition
Each def corresponds to a view which:
- receives a request url possibily with some passed parameters
- treats it
- returns the correct file template html to render and passes to it the correct parameters
Prototype:
def ***(request,attr1,...attrk)`            Defines a view ***
    operation1                              Examples  :
                                            get_object_or_404(Model,id) : returns a model of the type Model with the specified id
                                            form = ***Form(request.POST or None) : returns a form to be rendered with a request of type POST
    ...
    return ***view to return***
                                            Examples:
                                            render(request, 'file.html', locals()) : Renders a template named file.html and passes all the local variables to it
                                            redirect(***, PARAM) : Returns the view *** passing the parameters specified in PARAM

@login_required() : specifies that for such view the user has to be logged in. Otherwise it will redirect the user to the login page. Impplemantation of generic views
"""
# Basic django operations
from django.shortcuts import redirect, render, get_object_or_404
# Needed for generic views
from django.contrib.auth.decorators import login_required
# Don't forget to import models and forms!
from .models import Project, Task, Status, Journal
from .forms import JournalForm, NewTaskForm
# Useful for dates
from django.utils import timezone


# Create your views here.

# Home view : list of all projects of user user
@login_required()
def projects(request):
    user = request.user
    projects = user.project_set.all()
    return render(request, 'LifePlanner/projects.html', locals())


# Project view : list of all task of project project
@login_required()
def project(request, id_project):
    project = get_object_or_404(Project, id=id_project)
    # It takes all the tasks of the project project of the user
    tasks = project.task_set.all()
    return render(request, 'LifePlanner/project.html', locals())


# Task view: shows the details of the requested task
@login_required()
def task(request, id_task):
    user = request.user
    task = get_object_or_404(Task, id=id_task)
    project = task.project
    # It takes all the existing journals of the task task of the project project of the user user
    journals = task.journal_set.all()
    # Creation of a Journal form to be trated with a POST request
    form = JournalForm(request.POST)
    if form.is_valid():
        # In case all the entries of the form have been correctly filled in by the user a new journal is created to collect these data
        new_journal = Journal()
        new_journal.entry = form.cleaned_data['entry']
        # Date set by default at the moment of the fill
        new_journal.date = timezone.now()
        new_journal.author = user
        new_journal.task = get_object_or_404(Task, id=id_task)
        # Don't forget to save the journal
        new_journal.save()
    return render(request, 'LifePlanner/task.html', locals())


# Creation of task view : the user may fill a form for adding a new task to the project project
@login_required()
def create_task(request, id_project):
    # boolean isEditing is needed in the template to determine whether the user is modifying a task or creating a new one
    isEditing = False
    # Creation of a NewTask form to be trated with a POST request
    form = NewTaskForm(request.POST or None)
    project = get_object_or_404(Project, id=id_project)
    if form.is_valid():
        # In case all the entries of the form have been correctly filled in by the user a new task is created to collect these data
        new_task = Task()
        new_task.project = project
        new_task.name = form.cleaned_data['name']
        new_task.assigned = form.cleaned_data['assigned']
        new_task.description = form.cleaned_data['start_date']
        new_task.start_date = form.cleaned_data['start_date']
        new_task.due_date = form.cleaned_data['due_date']
        new_task.priority = form.cleaned_data['priority']
        # The status of a new task is set by default at New, irrespectively of what the user may choose if he as the possibility in the view
        new_task.status = Status.objects.get(name="New")
        new_task.save()

        return redirect(task, id_task=new_task.id)

    return render(request, 'LifePlanner/create_task.html', locals())


# Edition of task view : the user may change the values of an existing task of project project
@login_required()
def edit_task(request, id_project, id_task):
    # Task to edit
    current_task = get_object_or_404(Task, id=id_task)
    project = get_object_or_404(Project, id=id_project)
    # Instastation of an existing NewTask form which will be modified to be treated with a POST request
    form = NewTaskForm(request.POST or None, instance=current_task)
    # boolean isEditing is needed in the template to determine whether the user is modifying a task or creating a new one
    isEditing = True
    if form.is_valid():
        # In case all the entries of the form have been correctly filled in by the user the task is modified and saved
        current_task.Status = form.cleaned_data['status']
        form.save()
        return redirect(task, id_task=id_task)
    return render(request, 'LifePlanner/create_task.html', locals())
