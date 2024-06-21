from django.shortcuts import render
from django.http import HttpResponse

rooms= [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Frontend developer'},
]

# Create your views here.
def home(request):
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request):
    return render(request, 'base/room.html')