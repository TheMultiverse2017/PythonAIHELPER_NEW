from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    title = "Home"
    return render(request,'home.html',{'title':title})

def texttovoiceHome(request):
    title = "Text to Voice"
    return render(request,'texttovoice/home.html',{'title':title})

def texttovoiceConvert(request):
    title = "Text to Voice"
    message = "Error"
    return render(request,'texttovoice/home.html',{'title':title, 'message': message})