from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


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
