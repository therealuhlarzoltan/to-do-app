from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from tasks.forms import TaskCreationForm, ListCreationForm
from tasks.models import REPEAT_CHOICES, PRIOTRITY_CHOICES, Task

User = get_user_model()

# Create your views here.
@login_required
def homeView(request):
    return render(request, 'tasks/home.html')

@login_required
def createTaskView(request):
    qs = request.user.lists.all()
    lists = []
    for obj in qs:
        lists.append((obj.list, obj.list.capitalize()))
    users = []
    users = User.objects.all()
    context = {
        'title':'New Task',
        'priorities':PRIOTRITY_CHOICES,
        'repeats':REPEAT_CHOICES,
        'lists':lists,
        'users':users,
        'template_name':'components/task_creation_form.html'
    }
    return render(request, 'tasks/new.html', context)

@login_required
def createListView(request):
    context = {
        'title':'New List',
        'template_name':'components/list_creation_form.html'
    }
    return render(request, 'tasks/new.html', context)

@login_required
def editTaskView(request, id):
    qs = Task.objects.filter(id=id)
    if not qs.exists():
        return redirect(reverse('home'))
    if qs.first().owner != request.user:
        return redirect(reverse('home'))
    task_obj = qs.first()
    
    repeat = None
    priority = None

    for tuple in REPEAT_CHOICES:
        if task_obj.repeat in tuple:
            repeat = tuple
            break

    for tuple in PRIOTRITY_CHOICES:
        if task_obj.priority in tuple:
            priority = tuple
            break

    list = task_obj.list
    if not list:
        list = ('', 'None')
    else:
        list = (list.list, list.list.capitalize())

    assigned = None
    priorities = None
    repeats = None
    users = None
    lists = None


    
    
    
    
    
    
    
    
    
    
    context = {
        'repeat':repeat,
        'repeats':repeats,
        'priority':priority,
        'priorities':priorities,
        'assigned':assigned,
        'users':users,
        'list':list,
        'lists':lists,
        'task':task_obj,
        'title':'Edit Task',
        'template_name':'components/task_edit_form.html'
    }
    print(context)
    return render(request, 'tasks/edit.html', context)
