from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler

def index(request):
    return render(request, 'hello.html')
