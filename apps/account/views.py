from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from apps.account.form import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                messages.error(request, '登录失败')  # 暂时没用到
    return HttpResponseRedirect(reverse('home'))  # 返回首页


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
