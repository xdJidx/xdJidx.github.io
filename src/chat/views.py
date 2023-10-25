from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'tcp_gaming/home.html')

def room(request, room):
    username = request.GET.get('username')
    # Utilisation de get_object_or_404 pour gérer les cas où la salle n'existe pas.
    room_details = get_object_or_404(Room, name=room)
    return render(request, 'tcp_gaming/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        username = request.POST.get('username')

        if room_name and username:
            existing_room = Room.objects.filter(name=room_name).first()
            if existing_room:
                return redirect(f'/{room_name}/?username={username}')
            else:
                new_room = Room.objects.create(name=room_name)
                new_room.save()
                return redirect(f'/{room_name}/?username={username}')
        else:
            return HttpResponse("Veuillez fournir un nom de salle et un nom d'utilisateur valides.", status=400)
    else:
        return HttpResponse("Requête non autorisée", status=405)

def send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')

        if message and username and room_id:
            new_message = Message.objects.create(value=message, user=username, room_id=room_id)
            new_message.save()
            return HttpResponse('Message envoyé avec succès')
        else:
            return HttpResponse('Veuillez fournir un message, un nom d\'utilisateur et un ID de salle valides.', status=400)
    else:
        return HttpResponse("Requête non autorisée", status=405)

def getMessages(request,room):
    room_details = Room.objects.get(name = room)
    messages = Message.objects.filter(room=room_details).order_by('date')
    return JsonResponse({"messages": list(messages.values())})
