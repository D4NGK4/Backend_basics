from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello World")

def v1(response):
    return HttpResponse("Da first view")

# Create your views here.
