from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .forms import UserRegistrationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _("You are now logged in."))
            return redirect('list_reviews')
        else:
            messages.warning(request, _("Authentification has failed."))
            return redirect('login_user')
    else:
        return render(request, 'authentification/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, _("You have been logged out."))
    return redirect('login_user')


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, _("You have been registered."))
            return redirect('list_reviews')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentification/register.html', locals())
