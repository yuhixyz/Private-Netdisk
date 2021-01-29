from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from apps.account.form import LoginForm
from utils.tencent.cos import create_bucket, exist_bucket
from settings.dev import APPID
from .models import MyUser


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                bucket = '{}-{}'.format(user.uid.lower(), APPID)  # 注意uid转化为小写，更新桶名
                region = user.region
                if not exist_bucket(bucket, region):  # 桶不存在
                    create_bucket(bucket=bucket, region=user.region)  # 创建桶
                    MyUser.objects.filter(id=user.id).update(bucket=bucket)  # 写入数据库

    return HttpResponseRedirect(reverse('home'))  # 返回首页


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
