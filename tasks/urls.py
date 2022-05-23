from django.urls import path
from .views import homeView, createTaskView, createListView, editTaskView, editListView

urlpatterns = [
    path('', homeView, name='home'),
    path('new-task', createTaskView, name='new-task' ),
    path('new-list', createListView, name='new-list'),
    path('edit-task/<int:id>', editTaskView, name='edit-task'),
    path('edit-list/<int:id>', editListView, name='edit-list')
]
