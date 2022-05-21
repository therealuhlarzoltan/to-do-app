from django.conf import settings
from django.shortcuts import render, redirect

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..forms import ListCreationForm, TaskCreationForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create_view(request):
    form = TaskCreationForm(request.POST)
    if form.is_valid():
        task_obj = form.save(commit=False)
        task_obj.owner = request.user
        task_obj.save()
        return Response({}, status=201)
    return Response({}, status=400)

def task_delete_view(request):
    pass

def task_complete_view(request):
    pass

def task_edit_view(request):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def list_create_view(request):
    form = ListCreationForm(request.POST)
    if form.is_valid():
        list_obj = form.save(commit=False)
        list_obj.user = request.user
        list_obj.save()
        return Response({}, status=201)
    return Response({}, status=400)

def list_delete_view(request):
    pass