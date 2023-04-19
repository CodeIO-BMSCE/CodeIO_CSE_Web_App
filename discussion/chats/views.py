# from django.shortcuts import render, redirect
 
 
# def ChatPage(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("login")
#     context = {}
#     return render(request, "chat\live.html", context)

from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
from .models import Room, Message
from django.http import HttpResponse, JsonResponse, HttpRequest


# class ChatPage(TemplateView):
#     model = Chat
#     template_name = "chat/live.html"

# from django.shortcuts import render

# from .models import Message

# def index(request):
#     return render(request, 'chat\live.html')

# def room(request, room_name):
#     username = request.GET.get('username', 'Anonymous')
#     messages = Message.objects.filter(room=room_name)[0:25]

#     return render(request, 'chat/live.html', {'room_name': room_name, 'username': username, 'messages': messages})

def home(request):
    return render(request, 'chat/room.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/live.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    # username = HttpRequest.META
    # username = request.GET['object.username']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/livechat/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/livechat/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})