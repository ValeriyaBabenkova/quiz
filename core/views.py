from django.shortcuts import render, redirect, get_object_or_404
from .models import GamesList, Users, Theme, Answers, Questions
from .forms import AnswersAddForm
from django.contrib.auth import login as auth_login, get_user_model, authenticate, logout as auth_logout

from profiles.forms import LoginForm

def index(request):
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request, request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)

            return redirect('profiles_home')

    return render(request, 'index.html', {'login_form': login_form})
    # return render(request, 'index.html')
def games(request):
    theme_list = Theme.objects.all()
    games_list = GamesList.objects.all()

    print(games_list)

    theme = request.GET.get('theme')
    active_theme = None

    if theme:
        games_list = games_list.filter(theme__id=theme)
        active_theme = Theme.objects.get(id=theme)
    return render(request, 'games.html', {'games_list': games_list, 'theme_list': theme_list, 'active_theme': active_theme} )

def game(request, name_game_id):
    return render (request, 'game_detail.html')

def game_answers(request, name_game_id, num_tour, num_question):

    question_list= get_object_or_404(Questions,name_game_id=name_game_id, num_tour=num_tour, num_question=num_question)
    answer_team = AnswersAddForm()
    print(answer_team)

    if request.method == 'POST':
        print(request.POST)

        answer_team = AnswersAddForm(request.POST)
        answer_right = Questions.objects.get(id=num_question,name_game__id=name_game_id, num_tour=num_tour)
        print(answer_right.text)
        if answer_team.is_valid():
            answer_team = answer_team.save(commit=False)
            # answer_team.profile = request.user.profile

            print(bool(answer_team.answer_team.upper() == answer_right.text.upper()))


            return redirect('game_answers')

    return render(request, 'answers.html',
                  {'question': question_list, 'answer_team':answer_team})