from django.shortcuts import render

#useleess comment

from django.http import HttpResponse
def index (request):
    return HttpResponse("Rango says hey there partner! ")

def about (request):
    return HttpResponse("Rango says this is about! ")
