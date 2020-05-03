from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=150)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(verbose_name="Date de debut")
    due_date = models.DateTimeField(verbose_name="Date de fin")
    priority = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Track(models.Model):
#   name = models.CharField(max_length=200)
#  composer = models.CharField(max_length=220)
#   album = models.ForeignKey('Album', on_delete=models.CASCADE)
#   milliseconds = models.TextField()
#    bytes = models.IntegerField()
#   unitPrice = models.DecimalField(max_digits = 10, decimal_places = 2)

#   def __str__(self):
#       return self.name
