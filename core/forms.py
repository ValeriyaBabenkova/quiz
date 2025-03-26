from django import forms
from .models import Answers

class AnswersAddForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['answer_team']
