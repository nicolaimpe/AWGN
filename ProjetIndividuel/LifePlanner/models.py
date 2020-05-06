"""LifePlanner Models definition
Each class corresponds to a the definition of a model of the application
Prototype:
class ***(models.Model)`            creates a model ***
    attribute1 =
    ...
    class ***                       it's also possible to create classes
                                    Example
                                    class Meta:

    def ***(attribute of the definition)
                                    creation of functions within the model
                                    Example
                                    def__str__(self):  returns a string with the name of the model
"""
from django.db import models
# With this we do not need to define a User model to interact with the application, but rather we import it already done
from django.contrib.auth.models import User
# Limits the value of attributes of a model
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

# Project model
class Project(models.Model):
    name = models.CharField(max_length=150)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


# Status model : actually just the definition of the strings for the status
class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Task model
# Linked to both project and Status with ForeignKeys
class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    assigned = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Assigned")
    start_date = models.DateTimeField(verbose_name="Date de debut")
    due_date = models.DateTimeField(verbose_name="Date de fin")
    priority = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Journal model : To leave a comment on the page of tasks visualization
class Journal(models.Model):
    date = models.DateTimeField(verbose_name="Date de commentaire")
    entry = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
