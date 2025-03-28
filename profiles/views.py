from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, get_user_model, authenticate, logout as auth_logout

from .models import Profile
from .forms import LoginForm, RegisterForm

def profile(request):
    return render(request, 'profiles/home.html')


def login(request):
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request, request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)

            return redirect('profiles_home')

    return render(request, 'profiles/login.html', {'login_form': login_form})
def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # создали пользователя
            User = get_user_model()
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()

            # создать Profile
            Profile.objects.create(user=user)

            # залогинить
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)

            return redirect('profiles_home')

        # проверка валидности формы

    return render(request, 'profiles/register.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('index')