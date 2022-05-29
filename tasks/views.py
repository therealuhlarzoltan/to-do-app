from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from tasks.forms import TaskCreationForm, ListCreationForm
from tasks.models import REPEAT_CHOICES, PRIOTRITY_CHOICES, Task, List

repeat_choices = REPEAT_CHOICES
priority_choices = PRIOTRITY_CHOICES

User = get_user_model()

# Create your views here.
@login_required
def homeView(request):
    return render(request, 'tasks/home.html', {'user_id':request.user.id})

@login_required
def createTaskView(request):
    qs = request.user.lists.all()
    lists = []
    for obj in qs:
        lists.append((obj.id, obj.list.capitalize()))
    users = []
    users = User.objects.all()
    context = {
        'title':'New Task',
        'priorities':PRIOTRITY_CHOICES,
        'repeats':REPEAT_CHOICES,
        'lists':lists,
        'users':users,
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
    
    repeat = None
    priority = None

    if task_obj.repeat:
        for tuple in repeat_choices:
            if task_obj.repeat in tuple:
                repeat = tuple
                break

    if task_obj.priority:           
        for tuple in priority_choices:
            if task_obj.priority in tuple:
                priority = (str(tuple[0]), tuple[1])
                break

    list = task_obj.list
    lists = []
    if list:
        qs = request.user.lists.all().order_by('list').exclude(id=list.id)
    else:
        qs = request.user.lists.all().order_by('list')
    if qs.exists():
        serialized_lists = [list.serialize() for list in qs]
        for dict in serialized_lists:
            lists.append((dict.get('id'), dict.get('list').capitalize()))
        if list:
            list = (list.id, list.list.capitalize())

    if priority:
        og_priority = (int(priority[0]), priority[1])
        priorities = PRIOTRITY_CHOICES
        priorities.remove(og_priority)
    else:
        priorities = PRIOTRITY_CHOICES

    if repeat:
        repeats = REPEAT_CHOICES
        repeats.remove(repeat)
    else:
        repeats = REPEAT_CHOICES

    assigned = None
    qs = task_obj.assigned.all()
    if qs.exists():
        assigned_user_obj = qs.first()
        assigned = (assigned_user_obj.id, assigned_user_obj.username)



    users = None


    # TODO    
   


    context = {
        'default_repeat':repeat,
        'repeats':repeats,
        'default_priority':priority,
        'priorities':priorities,
        'assigned':assigned,
        'users':users,
        'default_list':list,
        'lists':lists,
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
    return render(request, 'tasks/list.html', {'title':list_obj.list, 'list_id':id})
