from django.urls import path
from .views import homeView, createTaskView, createListView

urlpatterns = [
    path('', homeView, name='home'),
    path('new-task', createTaskView, name='new-task' ),
    path('new-list', createListView, name='new-list'),
]
