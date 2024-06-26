from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room 
from .forms import RoomForm

#rooms= [
#    {'id':1, 'name':'Lets learn python!'},
#    {'id':2, 'name':'Design with me'},
#    {'id':3, 'name':'Frontend developer'},
# ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
     
def CreateRoom(request):
    print(request.POST) 
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
