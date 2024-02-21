from django.shortcuts import render, redirect
from .models import Room

# Create your views here.
def index(request):
    return render(request, "user/index.html")

def create_room(request):
    room = Room.objects.create()
    return redirect('room', room_id=room.id)

def room(request, room_id):
    room = Room.objects.get(id=room_id)
    players = room.player_set.all()
    context = {'room': room, 'players': players, 'room_id': room_id}
    return render(request, 'user/room.html', context)

def join_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        if room_id:
            return redirect('join_room_detail', room_id=room_id)
    return redirect('index')

def join_room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        if player_name:
            room.player_set.create(name=player_name)
            return redirect('room', room_id=room_id)
    return render(request, 'user/join_room_detail.html', {'room_id': room_id})