from django import forms

from .models import Task, List

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due', 'priority', 'list', 'assigned', 'repeat', 'end_repeat']

class ListCreationForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['list']