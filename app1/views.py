from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def King(request):
    return HttpResponse('Welcome to My Kingdom!')
