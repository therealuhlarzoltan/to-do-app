from django import forms

from .models import Task, List

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due', 'priority', 'list', 'assigned', 'repeat', 'end_repeat']

    def clean(self):
        cleaned_data = super().clean()
        repeat = cleaned_data.get("repeat")
        due = cleaned_data.get("due")

        if repeat and not due:
            raise forms.ValidationError("Submitted repeat interval without submitting due date.")

class ListCreationForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['list']