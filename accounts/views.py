from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from accounts.forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sign-in')
    elif request.method == 'GET':
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    if request.method == 'GET':
        return render(request, 'accounts/signin.html')


def user_logout(request):
    # 로그아웃 view
    pass
