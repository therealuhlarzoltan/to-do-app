from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from tasks.forms import TaskCreationForm, ListCreationForm
from tasks.models import REPEAT_CHOICES, PRIORITY_CHOICES, Task, List

from .repeat import repeat_task

repeat_choices = REPEAT_CHOICES
priority_choices = PRIORITY_CHOICES

User = get_user_model()

# Create your views here.
@login_required
def homeView(request):
    qs = Task.objects.filter(owner=request.user, completed=True, repeat=None)
    if qs.exists():
        qs.delete()
    qs1 = Task.objects.filter(owner=request.user, completed=True).exclude(repeat=None)
    if qs1.exists():
        for task in qs1:
            repeat_task(task)
    return render(request, 'tasks/home.html', {'user_id':request.user.id})

@login_required
def createTaskView(request):
    qs = request.user.lists.all()
    lists = []
    for obj in qs:
        lists.append((obj.id, obj.list.capitalize()))
    context = {
        'title':'New Task',
        'priorities':PRIORITY_CHOICES,
        'repeats':REPEAT_CHOICES,
        'lists':lists,
        'template_name':'components/task_creation_form.html',
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
    
    
    lis = task_obj.list
    lists = []
    if lis:
        qs = request.user.lists.all().order_by('list').exclude(id=lis.id)
    else:
        qs = request.user.lists.all().order_by('list')
    if qs.exists():
        serialized_lists = [lis.serialize() for lis in qs]
        for dict in serialized_lists:
            lists.append((dict.get('id'), dict.get('list').capitalize()))
        if lis:
            lis = (lis.id, lis.list)


    priority = None
    priorities = []

    if task_obj.priority:   
        if task_obj.priority == 1:
            priority = 1
        if task_obj.priority == 2:
            priority = 2    
        if task_obj.priority == 3:
            priority = 3          
        
    else:
        priorities = [
            ('', 'None'),
            (1, 'Not Important'),
            (2, 'Important'),
            (3, 'Very Important')
        ]

    if priority:
        if priority == 1:
            priorities = [
            (1, 'Not Important'),
            (2, 'Important'),
            (3, 'Very Important'),
            ('', 'None')
        ]
        if priority == 2:
           priorities = [
            (2, 'Important'),
            (1, 'Not Important'),
            (3, 'Very Important'),
            ('', 'None')
        ]
        elif priority == 3:
            priorities = [
            (3, 'Very Important'),
            (1, 'Not Important'),
            (2, 'Important'),
            ('', 'None')
        ]
            
    
    repeat = None
    repeats = None
    
    if task_obj.repeat:
        repeat = task_obj.repeat

    if repeat:
        repeats = REPEAT_CHOICES
        repeat_tuple = list(filter(lambda r: r[0] == repeat, repeats))
        sorted = list(filter(lambda r: r[0] != repeat, repeats))
        if not ('', 'None') in sorted:
            sorted.append(('', 'None'))
        if not repeat_tuple[0] in sorted:
            sorted.insert(0, repeat_tuple[0])
        repeats = sorted
    else:
        repeats = REPEAT_CHOICES
        if not ('', 'None') in repeats:
            repeats.insert(0, ('', 'None'))

    due = task_obj.due
    if not due:
        due = ''

    end_repeat = task_obj.end_repeat
    if not end_repeat:
        end_repeat = ''


    context = {
        'repeats':repeats,
        'priorities':priorities,
        'default_list':lis,
        'lists':lists,
        'due':due,
        'end_repeat':end_repeat,
        'task':task_obj,
        'title':'Edit Task',
        'template_name':'components/task_edit_form.html'
    }
    return render(request, 'tasks/edit.html', context)

@login_required
def editListView(request, id):
    qs = List.objects.filter(id=id)
    if not qs.exists():
        return redirect(reverse('home'))
    if qs.first().user != request.user:
        return redirect(reverse('home'))
    list_obj = qs.first()
    context = {
        'template_name':'components/list_edit_form.html',
        'list':list_obj,
        'title':'Edit List'
    }

    return render(request, 'tasks/edit.html', context)


@login_required
def listView(request, id):
    qs = List.objects.filter(id=id)
    if not qs.exists():
        return redirect(reverse('home'))
    list_obj = qs.first()
    if list_obj.user != request.user:
        return redirect(reverse('home'))
    qs1 = Task.objects.filter(owner=request.user, completed=True, list=list_obj)
    if qs1.exists():
        qs1.delete()
    qs2 = Task.objects.filter(owner=request.user, completed=True, list=list_obj).exclude(repeat=None)
    if qs2.exists():
        for task in qs2:
            repeat_task(task)
    return render(request, 'tasks/list.html', {'title':list_obj.list, 'list_id':id})


@login_required
def listsView(request):
    qs = List.objects.all().filter(user=request.user).order_by('timestamp')
    return render(request, 'tasks/lists.html', {'lists':qs})
