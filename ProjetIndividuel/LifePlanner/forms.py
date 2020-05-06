"""LifeManager Forms definition


The `***Form(forms.ModelForm)` creates a form based on model ***.
It's possible to specify the fields and charateristics taken into account

Examples:
    1. fields = '__all__' : One field for each attribute of the model
    2. widgets = Determine the tye of input on the rendered form when passed through a view

"""

from django import forms
# Don't forget to import the models you want to make a form from!
from .models import Task, Journal


# Form for the model journal : add updates to the task when the latter is visualized
class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ('entry',)


# Form for a task model
# Despite the name you can use it also for an existing task
class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        # Dates are gonna be rendered in the form through widget rather than text
        widgets = {'start_date': forms.SelectDateWidget,
                   'due_date': forms.SelectDateWidget}
