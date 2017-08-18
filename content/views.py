from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CommentForm, RegisterForm, SearchForm, SetInForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'index.html')


def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # 登录成功跳转主页
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'form': form, 'error': 'username or password incorrect'})

        return render(request, 'login.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
