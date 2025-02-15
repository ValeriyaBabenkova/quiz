from django.shortcuts import render
from .models import GamesList, Users, Theme

# Create your views here.
def index(request):
    return render(request, 'index.html')
def games(request):
    theme_list = Theme.objects.all()
    games_list = GamesList.objects.all()
    return render(request, 'games.html', {'games_list': games_list, 'theme_list': theme_list} )