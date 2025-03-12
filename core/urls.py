from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('games/<int:name_game_id>', views.game_answers, name='game_answers'),
]