from django.shortcuts import render
from django.http import HttpResponse

def index(request, path=''):
    return render(request, 'index.html')