from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room 

# Create your views here.

@login_required
def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms':rooms
    }
    return render(request,'chat/home.html',context)

@login_required
def room(request,id):
    room = Room.objects.get(id=id)
    messages = room.messages.all()
    
    context = { 
        'room':room,
        'messages':messages
    }
    return render(request,'chat/room.html',context)
