from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('players/', views.players, name='players'),
    path('players/<int:pk>/edit/', views.player_edit, name='player_edit'),
    path('players/new/',views.player_new, name='player_new'),
    path('playerDelete/<int:pk>/', views.player_delete, name="player_delete"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('gamepage/', views.game_page, name='game_page'),
]
