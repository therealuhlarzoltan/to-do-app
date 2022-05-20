from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homeView(request):
    return HttpResponse("Home")