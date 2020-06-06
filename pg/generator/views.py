from django.shortcuts import render
from django.http import HttpResponse
import random

# # Create your views here.
# def home(request):
#     return HttpResponse('hello and welcome to this project')

# def index(request):
#     return HttpResponse('<h1>I am trying out another page</h1>')

def home(request):
    return render(request, 'generator/home.html')


def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = 10

    thepassword = ''

    for x in range(length):
        thepassword+= random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})


def about(request):
    return render(request, 'generator/about.html')