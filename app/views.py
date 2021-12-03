from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.
from app.models import DBFeedback, DBLinkAll, DBProject


@login_required(login_url='/login')
def home(request):
    # if request.user.is_authenticated:
    data = DBLinkAll.objects.all()
    return render(request, 'index.html', {'user': User.username, "data": data})
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
            user_new = User.objects.create_user(username=username, password=passwd)
            user_new.save()
            return HttpResponse('注册成功')
        except BaseException:
            return HttpResponse('用户名重复或违反规定')
    else:
        return redirect('/login')


def logout(request):
    auth.logout(request)
    return redirect('/login')


def feedback(request):
    if request.method == 'GET':
        data = request.GET['feedback_value']
        DBFeedback.objects.create(user=request.user.username, text=data)
        return HttpResponseRedirect('')


def help_doc(request):
    return render(request, 'help.html')


def link_all(request):
    data = DBLinkAll.objects.all()
    return render(request, 'index.html', {'data': data})


def child(request, eid, oid):
    res = child_json(eid)
    print(eid)
    return render(request, eid, res)


def child_json(eid):
    if eid == 'index.html':
        date = DBLinkAll.objects.all()
        res = {"hrefs": date}
        return res


def project_list(request):
    data = DBProject.objects.all()
    return render(request, 'project.html', {'data': data})


def del_project(request, id):
    DBProject.objects.get(id=id).delete()
    return redirect('app:project_list')


def add_project(request):
    project_name = request.GET['project_name']
    DBProject.objects.create(name=project_name, remark='', user=request.user.username, user_id='', other_user='')
    return HttpResponse('')


def apis(request, id):
    project_id = id
    return render(request, 'index.html')


def apis_detail(request, id):
    api_info = DBProject.objects.get(id=id)
    context = {'api_info': api_info}
    return render(request, 'p_apis.html', context)


def get_project_set(request, id):
    project_set = DBProject.objects.get(id=id)
    context = {'project': project_set}
    return render(request, 'p_project_set.html', context)


def save_project_set(request, id):
    project_set = DBProject.objects.filter(id=id)
    name = request.GET['name']
    remark = request.GET['remark']
    other_user = request.GET['other_user']
    project_set.update(name=name, remark=remark, other_user=other_user)
    return HttpResponse('')
