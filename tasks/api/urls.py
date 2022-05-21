from django.urls import path

from .views import task_create_view, list_create_view

urlpatterns = [
    path('create-task/', task_create_view, name='task-create-api'),
    path('create-list/', list_create_view, name='list-create-api'),

]
