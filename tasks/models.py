from pyexpat import model
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

PRIOTRITY_CHOICES = [
    (1, 'Not important'),
    (2, 'Important'),
    (3, 'Very important')
]

REPEAT_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('biweekly', 'Biweekly'),
    ('monthly', 'Monthly'),
    ('3months', 'Every 3 Months'),
    ('6months', 'Every 6 Months'),
    ('yearly', 'Yearly')
]

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.SmallIntegerField(choices=PRIOTRITY_CHOICES, null=True, blank=True)
    repeat = models.CharField(choices=REPEAT_CHOICES, null=True, blank=True, max_length=16)
    end_repeat = models.DateField(auto_now=False, auto_now_add=False, null=True)
    assigned = models.ManyToManyField(User, related_name="assignments", blank=True, null=True, through='Assignment')
    list = models.ForeignKey('List', on_delete=models.CASCADE, blank=True, null=True)

class Assignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class List(models.Model):
    list = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE)

class ListAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)