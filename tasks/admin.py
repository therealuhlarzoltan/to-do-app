from django.contrib import admin

from .models import Task, List, Assignment

# Register your models here.
admin.site.register(Task)
admin.site.register(List)
admin.site.register(Assignment)