from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def lucas(request):
    return render(request, 'myapp/lucas.html')

def felipe(request):
    return render(request, 'myapp/felipe.html')