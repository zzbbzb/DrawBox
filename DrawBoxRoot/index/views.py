from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<html><body><a href='/'>Hello World</a><body></html>")
