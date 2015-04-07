from django import forms
from Organizer import models

class TMDateInput(forms.DateInput):
    input_type = 'date'

class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ('id', 'name', 'abbreviation', 'limited')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('id', 'name', 'client', 'priority')

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ('id', 'title', 'project', 'severity', 'due')
        widgets = {
            'title': forms.TextInput,
            'due': TMDateInput,
        }
