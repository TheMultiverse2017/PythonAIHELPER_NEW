from django.shortcuts import render
from django.http import HttpResponse

def loginIndex(request):
    title = "Login"
    return render(request,'reg_login/login.html',{'title':title})

def loginSubmit(request):
    message = "Error"
    if request.method == 'POST':
        email =  request.POST.get('email')
        password =  request.POST.get('password')
        confirm_password =  request.POST.get('confirm_password')

def regIndex(request):
    title = "Register"
    return render(request,'reg_login/register.html',{'title':title})

def regSubmit(request):
    message = "Error"
    if request.method == 'POST':
        email =  request.POST.get('email')
        password =  request.POST.get('password')