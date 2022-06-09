from django import forms

from .models import Task, List

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due', 'priority', 'list', 'repeat', 'end_repeat', 'owner']

    def clean(self):
        cleaned_data = super().clean()
        repeat = cleaned_data.get("repeat")
        due = cleaned_data.get("due")
        owner = cleaned_data.get("owner")
        list = cleaned_data.get("list")


        if repeat and not due:
            raise forms.ValidationError("Submitted repeat interval without submitting due date.")

        if list:
            if list.id not in List.objects.filter(user=owner).values_list('id', flat=True):
                raise forms.ValidationError("Invalid list.")


        

class ListCreationForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['list']