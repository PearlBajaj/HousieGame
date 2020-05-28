from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Player
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def dashboard(request):
    players = Player.objects.all()[:10]
    return render(request, 'housie/dashboard.html',{'players':players})

def players(request):
    players = Player.objects.all()
    return render(request, 'housie/players.html',{'players':players})

def player_edit(request,pk):
    player = get_object_or_404(Player,pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player.name = form.cleaned_data['player_name']
            player.email= form.cleaned_data['player_email']
            player.no_tickets = form.cleaned_data['player_no_tickets']
            player.save()
            return redirect('players')
    else:
        form = PlayerForm(initial={'player_name': player.name, 'player_email': player.email, 'player_no_tickets': player.no_tickets})
    return render(request, 'housie/player_edit.html', {'form': form})

def player_new(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if(form.is_valid()):
            player = Player()
            player.name = form.cleaned_data['player_name']
            player.email = form.cleaned_data['player_email']
            player.no_tickets = form.cleaned_data['player_no_tickets']
            player.save()
            return redirect('players')
    else:
        form = PlayerForm()

    return render(request,'housie/player_edit.html',{'form': form})


def player_delete(request,pk):
    player = get_object_or_404(Player,pk=pk)
    player.delete()
    return redirect('players')

def game_page(request):
    return render(request, 'housie/gamepage.html')
