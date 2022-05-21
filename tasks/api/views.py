from django.conf import settings
from django.shortcuts import render, redirect

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..forms import ListCreationForm, TaskCreationForm

from ..models import Task, List

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create_view(request):
    form = TaskCreationForm(request.POST)
    if form.is_valid():
        task_obj = form.save(commit=False)
        task_obj.owner = request.user
        task_obj.save()
        return Response({"message":"Task created!"}, status=201)
    return Response({}, status=400)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def task_delete_view(request, id):
    qs = Task.objects.filter(id=id)
    if not qs.exists():
        return Response({'message':'Task does not exist.'}, status=400)
    task_obj = qs.first()
    if request.user != task_obj.owner:
        return Response({'message':'Forbidden.'}, status=403)
    task_obj.delete()
    return Response({}, status=200)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def task_complete_view(request, id):
    qs = Task.objects.filter(id=id)
    if not qs.exists():
        return Response({'message':'Task does not exist'}, status=400)
    task_obj = qs.first()
    if request.user != task_obj.owner:
        return Response({'message':'Forbidden'}, status=403)
    task_obj.completed = not task_obj.completed
    task_obj.save()
    return Response({'completed':task_obj.completed}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
        return Response({"message":"List created!"}, status=201)
    return Response({}, status=400)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def list_delete_view(request, id):
    qs = List.objects.filter(id=id)
    if not qs.exists():
        return Response({'message':'List does not exist.'}, status=400)
    list_obj = qs.first()
    if request.user != list_obj.user:
        return Response({'message':'Forbidden.'}, status=403)
    list_obj.delete()
    return Response({}, 200)