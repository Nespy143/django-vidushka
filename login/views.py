from lib2to3.fixes.fix_input import context
from django.contrib.auth import authenticate, logout, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from . import forms
from .forms import RegisterForm


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            redirect('/login/')
    return render(request, 'login/login.html')


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = forms.RegisterForm()
        context = {'form': form}
        return render(request, 'login/register.html', context)

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        context = {'form': form}
        return render(request, 'login/register.html', context)


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("/")