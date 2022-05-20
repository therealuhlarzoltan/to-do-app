from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tasks.forms import TaskCreationForm

# Create your views here.
@login_required
def homeView(request):
    return render(request, 'tasks/home.html')

def createTaskView(request):
    context = {
        'title':'New Task',
        'form':TaskCreationForm,
        'template_name':'components/task_creation_form.html'
    }
    return render(request, 'tasks/new.html', context)