from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def secure(request):
    return HttpResponse("This is a secure page with no vulnerabilities.")
