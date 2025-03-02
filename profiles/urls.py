from django.urls import path

from . import views

urlpatterns = [
    path('profile', views.profile, name='profiles_home'),
    path('login', views.login, name='profiles_login'),
    path('register', views.register, name='profiles_register'),
    path('logout', views.logout, name='profiles_logout')

]
