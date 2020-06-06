from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.
# def home(request):
#     return HttpResponse('hello and welcome to this project')

# def index(request):
#     return HttpResponse('<h1>I am trying out another page</h1>')

def home(request):
    return render(request, 'generator/home.html')