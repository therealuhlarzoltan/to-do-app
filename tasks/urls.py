from django.urls import path
from .views import homeView, createTaskView

urlpatterns = [
    path('', homeView, name='home'),
    path('new-task', createTaskView, name='new-task' )
]
