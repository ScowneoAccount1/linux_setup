from multiprocessing import context
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
# from django.http import HttpResponse
from .models import Room
# Create your views here.


# rooms = [
#     {'id': 1, 'name':"Let's learn python!"},
#     {'id': 2, 'name':"Design w me!"}, 
#     {'id': 3, 'name':"Let's learn C sharp!"}, 
# ]
 

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i

    room = Room.objects.get(id=pk)

    context = {'room': room}

    return render(request, 'base/room.html', context)


# app templates are inside of app folder
# templates (navbar and  etc.) are incide of root folder