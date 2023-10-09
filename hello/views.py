from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hi, Good evening! I'm learning Azure Cloud computing, and its very interesting! ")
