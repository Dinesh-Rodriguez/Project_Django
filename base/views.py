from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
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
     
def createRoom(request):
    form = RoomForm()
    topics =Topic.objects.all()
    if request.method =='POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description= request.POST.get('description')

        )


        #form = RoomForm(request.POST)
        # if form.is_valid():
        #    room =form.save(commit=False)
        #    room.host = request.user
        #    room.save()
        return redirect('home')
         

    context={'form':form, 'topics':topics }
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics =Topic.objects.all()

    if request.user != room.host:
            return HttpResponse('You are not allowed here!')

    if request.method == 'POST' :

       topic_name = request.POST.get('topic')
       topic, created = Topic.objects.get_or_create(name=topic_name)
       room.name =request.POST.get('name')
       room.topic =topic
       room.description =request.POST.get('description')
       room.save()
       return redirect('home')

    context ={'form':form,'room':room, 'topics':topics}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk) :
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render (request, 'base/delete.html', {'obj': room})

