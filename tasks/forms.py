from django import forms

from .models import Task

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due', 'priority', 'list', 'assigned', 'repeat', 'end_repeat']