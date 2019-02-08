from django.shortcuts import render

from django.http import HttpResponse

def printHello(request):
    return HttpResponse('hello from mrinal to django')

# Create your views here.
