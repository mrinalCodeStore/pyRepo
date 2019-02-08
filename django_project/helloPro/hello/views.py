from django.shortcuts import render
from django.http import HttpResponse


def printHello(request):
	return HttpResponse('ok this time for sure hello')

# Create your views here.
