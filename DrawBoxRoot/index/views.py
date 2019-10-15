from django.shortcuts import render
from django.http import HttpResponse
from .models import DrawBox

# Create your views here.
def index(request):
    drawBoxes = DrawBox.objects.all()
    
    return render(request, "index/index.html", {'drawBoxes' : drawBoxes})
