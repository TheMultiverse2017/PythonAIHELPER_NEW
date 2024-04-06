from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    title = "Home"
    return render(request,'home.html',{'title':title})
