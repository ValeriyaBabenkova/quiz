from django.shortcuts import render, redirect
from .models import GamesList, Users, Theme, Answers, Questions
from .forms import AnswersAddForm

def index(request):
    return render(request, 'index.html')
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

def answers(request):
    answers_form = AnswersAddForm(request.POST)
    question_list = Questions.objects.all()


    if request.method == 'POST':
        answers_form = AnswersAddForm()
        if answers_form.is_valid():
            team = answers_form.cleaned_data['team']
            answer_team = answers_form.cleaned_data['answer_team']
            answer_right = answers_form.cleaned_data['answer_right']
            Answers.objects.create(team=team, answer_team=answer_team, answer_right=answer_right)
            return redirect('Ваш ответ принят')

    return render(request, 'answers.html', {'question_list': question_list, 'answers_form': answers_form}, )