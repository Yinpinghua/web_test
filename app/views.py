from django.shortcuts import render,redirect

from app import  models

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello World!')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user_obj = models.User.objects.filter(user_name=name,password=pwd).first()
        if user_obj:
            return redirect("http://127.0.0.1:8000/hello")
        else:
            return HttpResponse('用户名或密码错误')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        re_pwd = request.POST.get('re_pwd')
        if name and pwd and re_pwd:
            if pwd == re_pwd:
                user_obj = models.User.objects.filter(user_name=name).first()
                if user_obj:
                    return HttpResponse('用户已存在')
                else:
                    models.User.objects.create(user_name=name,password=pwd).save()
                    return redirect('/login/')
            else:
                return HttpResponse('两次密码不一致')

        else:
            return HttpResponse('不能有空！')
