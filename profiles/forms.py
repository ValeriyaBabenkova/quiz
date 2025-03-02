from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):

        super(LoginForm, self).__init__(*args, **kwargs)
        self.request = request
        self.user = None

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        self.user = authenticate(self.request, username=username, password=password)

        if not self.user:
            raise ValidationError('Неверный логин или пароль')

    def get_user(self):
        return self.user

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    password_control = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        password = self.cleaned_data['password']
        password_control = self.cleaned_data['password_control']

        if password != password_control:
            raise ValidationError('Пароли не совпадают!')

    def clean_username(self):
        username = self.cleaned_data['username']
        User = get_user_model()

        if User.objects.filter(username=username).exists():
            raise ValidationError('Такой пользователь уже есть')
        return username

