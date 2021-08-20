from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth


# Create your views here.

@login_required(login_url='/login')
def home(request):
    # if request.user.is_authenticated:
    return render(request, 'index.html', {'user': User.username})
    # else:
    #     return redirect('/login')


def login_user(request):
    if request.method == "POST":
        username = request.POST['inputUsername']
        passwd = request.POST['inputPassword']
        data_user = auth.authenticate(username=username, password=passwd)
        if data_user is not None:
            login(request, data_user)
            return redirect('/')
        else:
            return render(request, 'logo.html', {'info': '账号或密码错误'})
    else:
        return render(request, 'logo.html')


def register_user(request):
    if request.method == "POST":
        username = request.POST['inputUsername']
        passwd = request.POST['inputPassword']
        try:
            User.objects.create_user(username=username, password=passwd)
            User.save()
            return HttpResponse('<script>alert(注册成功)</script>')
        except:
            return HttpResponse('<script>alert(注册失败，用户名可能重复了！）</script>')
    else:
        return redirect('/login')


def logout(request):
    auth.logout(request)
    return redirect('/login')