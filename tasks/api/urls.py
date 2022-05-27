from django.urls import path

from .views import task_create_view, list_create_view, list_delete_view, task_delete_view, task_complete_view, task_edit_view, list_edit_view, today_task_view

urlpatterns = [
    path('create-task/', task_create_view, name='task-create-api'),
    path('delete-task/<int:id>', task_delete_view, name='task-delete-api'),
    path('edit-task/<int:id>', task_edit_view, name='task-edit-api'),
    path('complete-task/<int:id>', task_complete_view, name='task-complete-api'),
    path('create-list/', list_create_view, name='list-create-api'),
    path('delete-list/<int:id>', list_delete_view, name='list-delete-api'),
    path('edit-list/<int:id>', list_edit_view, name='list-edit-api'),
    path('user/<int:id>/', today_task_view, name='task-today-api'),

]
