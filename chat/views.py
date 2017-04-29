import random
import string
from django.db import transaction
from django.shortcuts import render_to_response,render, redirect
import haikunator
from .models import Room
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required


def about(request):
    return render(request, "chat/about.html")

@login_required(login_url='/accounts/login/')
def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    
    new_room = None

    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect(chat_room, label=label)
    '''
    room = request.GET['room_name']
    print("This is a new Room Request: Room name",room)
    return redirect(chat_room, label=room)
    '''


@login_required(login_url='/accounts/login/')
def chat_room(request, label):
    """
    Room view - show the room, with latest messages.

    The template for this view has the WebSocket business to send and stream
    messages, so see the template for where the magic happens.
    """
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    
    #room, created = Room.objects.get_or_create(label=label)
    try:
        room = Room.objects.get(label=label)
    except Room.DoesNotExist:
        room = None

    if room ==None:
        return render_to_response('includes/error.html')


    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('timestamp')[:30])

    #Finding and loading all the rooms in the database
    all_rooms = Room.objects.all()
    '''for r in all_rooms:
        if r.label != 'accounts':
            if r.label != 'loggedin':
                print(r.label)
    '''
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
        'all_rooms': all_rooms,
        'username': username,
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
         form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')

def loggedin(request):
    all_rooms = Room.objects.all()

    username = None
    if request.user.is_authenticated():
        username = request.user.username

    return render(request,'registration/loggedin.html',{
            'all_rooms':all_rooms,
            'username': username,
        })