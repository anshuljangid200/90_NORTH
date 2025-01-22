from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import User, Message

@login_required
def chat_list(request):
       users = User.objects.exclude(id=request.user.id)
       return render(request, 'chat/chat_list.html', {'users': users})

@login_required
def chat_room(request, username):
    other_user = get_object_or_404(User, username=username)
    # Fetch messages between the logged-in user and the other user
    messages = Message.objects.filter(
        sender=request.user, receiver=other_user
    ) | Message.objects.filter(
        sender=other_user, receiver=request.user
    ).order_by('timestamp')
    
    return render(request, 'chat/chat_room.html', {
        'other_user': other_user,
        'messages': messages,
    })