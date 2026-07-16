from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic


# It gives the same page, after post request, set the user in db
class UserLoginView(LoginView):


    template_name = 'accounts/login.html'
    
class UserRegisterView(generic.CreateView):
    pass

class UserLogoutView(LogoutView):
    next_page = 'accounts:login'
