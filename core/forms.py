from django import forms
from .models import Answers

class AnswersAddForm(forms.Form):
    answer_team = forms.CharField(label='Введите ваш ответ:')