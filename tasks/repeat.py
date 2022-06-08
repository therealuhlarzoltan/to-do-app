import datetime

from .models import Task

def create_new_task(task, due):
    new_task = Task.objects.create(
                owner=task.owner, 
                task=task.task,
                priority=task.priority,
                repeat=task.repeat,
                #assigned=task.assigned,
                list=task.list,
                end_repeat=task.end_repeat,
                due=due
                )


def repeat_task(task):
    if task.repeat == 'daily':
        due_date = task.due
        due_date = task.due + datetime.timedelta(days=1)
        if not task.end_repeat:
            create_new_task(task, due_date)
            task.delete()
        else:
            if due_date > task.end_repeat:
                task.delete()
            else:
                create_new_task(task, due_date)
                task.delete()
    if task.repeat == 'weekly':
        due_date = task.due
        due_date = task.due + datetime.timedelta(days=7)
        if not task.end_repeat:
            create_new_task(task, due_date)
            task.delete()
        else:
            if due_date > task.end_repeat:
                task.delete()
            else:
                create_new_task(task, due_date)
                task.delete()
    if task.repeat == 'biweekly':
        due_date = task.due
        due_date = task.due + datetime.timedelta(days=14)
        if not task.end_repeat:
            create_new_task(task, due_date)
            task.delete()
        else:
            if due_date > task.end_repeat:
                task.delete()
            else:
                create_new_task(task, due_date)
                task.delete()
    if task.repeat == 'monthly':
        due_date = task.due
        due_date = task.due + datetime.timedelta(months=1)
        if not task.end_repeat:
            create_new_task(task, due_date)
            task.delete()
        else:
            if due_date > task.end_repeat:
                task.delete()
            else:
                create_new_task(task, due_date)
                task.delete()
    if task.repeat == '3months':
        due_date = task.due
        due_date = task.due + datetime.timedelta(months=3)
        if not task.end_repeat:
            create_new_task(task, due_date)
            task.delete()
        else:
            if due_date > task.end_repeat:
                task.delete()
            else:
                create_new_task(task, due_date)
                task.delete()
    if task.repeat == '6months':
        due_date = task.due
        due_date = task.due + datetime.timedelta(months=6)
        if not task.end_repeat:
            create_new_task(task, due_date)
            task.delete()
        else:
            if due_date > task.end_repeat:
                task.delete()
            else:
                create_new_task(task, due_date)
                task.delete()
    if task.repeat == 'yearly':
        due_date = task.due
        due_date = task.due + datetime.timedelta(years=1)
        if not task.end_repeat:
            create_new_task(task, due_date)
            task.delete()
        else:
            if due_date > task.end_repeat:
                task.delete()
            else:
                create_new_task(task, due_date)
                task.delete()
