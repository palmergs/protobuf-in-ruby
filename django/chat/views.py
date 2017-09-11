from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'chat/index.html', {})

def secure(request):
    return HttpResponse("This is a secure page with no vulnerabilities.")
