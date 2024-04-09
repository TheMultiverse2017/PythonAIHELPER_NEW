from django.shortcuts import render
from django.http import HttpResponse
from text_to_speech.TOOLS.helpers import *

def storygenerator(request):
    title = "Story Generator"
    all_voices = allvoicesForTikTok()
    return render(request,'storygenerator/home.html',{'title':title, 'all_voices':all_voices})


def generateStory(request):
    title = "Story Generator : Initial Result"
    message = "Error"
    if request.method == 'POST':
        text =  request.POST.get('text')
        ttsselected =  request.POST.get('imageCount')

        return render(request,'storygenerator/initialResult.html',{'title':title})


    return HttpResponse("story generator")