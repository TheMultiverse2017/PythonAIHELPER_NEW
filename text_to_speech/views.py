from django.shortcuts import render
from django.http import HttpResponse
from .TTS.GTTS import GTTS
from .TTS.TikTok import TikTok
from .TTS.PYTTS import PYTTS
from .TOOLS.audioMerge import merge_audio_files
import random
from .TOOLS.createDir import *
from .TOOLS.helpers import *

def texttovoiceHome(request):
    title = "Text to Voice"
    all_voices = allvoicesForTikTok()
    return render(request,'texttovoice/home.html',{'title':title, 'all_voices':all_voices})

def texttovoiceConvert(request):
    title = "Text to Voice"
    message = "Error"
    if request.method == 'POST':
        text =  request.POST.get('text')
        ttsselected =  request.POST.get('tts')
        dirSub = random.randint(1,1000)
        output_filename = 'output_audio.mp3'
        if text:
            # Save the generated speech to the specified output path
            if ttsselected == 'GTTS':
                tts = GTTS()

                dir = 'CONVERTED_TEXT_TO_AUDIO/'+ttsselected+'/'+str(dirSub)+'/'
                createDir(dir)
                output_full_path = joinDirwithPath(dir, output_filename = 'output_audio.mp3')

                tts.run(text=text, filepath=output_full_path)
                downloadAudio(dir)
                message = 'Success'
            elif ttsselected == 'TIKTOK':
                tiktok_voice = request.POST.get('tiktok_voice') or 'en_us_001'
                tiktok_sessionid = '77f91489cd95fd25093fc443fb311cd0'
                tts = TikTok(tiktok_sessionid, tiktok_voice)

                if  len(text)>150:
                    # Split the text into individual words
                    words = text.split()
                    # Initialize an empty list to store groups of words as sentences
                    sentence_groups = []
                    current_sentence = ""
                    a=0
                    dir = 'CONVERTED_TEXT_TO_AUDIO/'+ttsselected+'/'+str(dirSub)+'/temp/'
                    createDir(dir)
                    # Combine every 10 words into a single sentence
                    for i, word in enumerate(words):
                        # Add the current word to the current sentence
                        current_sentence += word + ' '

                        # Check if we've reached the end of a sentence (every 10 words)
                        if (i + 1) % 10 == 0:
                            # Append the completed sentence to the sentence_groups list
                            sentence_groups.append(' '+current_sentence.strip())

                            output_full_path = joinDirwithPath(dir, output_filename = 'tiktok_audio_'+str(a)+'.mp3')

                            tts.run(text=current_sentence, filepath=output_full_path)
                            # Reset the current_sentence variable for the next sentence
                            current_sentence = " "
                            a+=1
                    # Append any remaining words as a last sentence
                    if current_sentence:
                        sentence_groups.append(current_sentence.strip())

                        output_full_path = joinDirwithPath(dir, output_filename = 'tiktok_audio_'+str(a)+'.mp3')

                        tts.run(text=current_sentence, filepath=output_full_path)

                    merge_audio_files(dir)
                    # Now sentence_groups contains your desired result
                    # return HttpResponse(sentence_groups)
                    message = 'Success'
                    I
                else:
                    dir = 'CONVERTED_TEXT_TO_AUDIO/'+ttsselected+'/'+str(dirSub)+'/'
                    createDir(dir)

                    output_full_path = joinDirwithPath(dir, output_filename = 'tiktok_audio.mp3')

                    tts.run(text=text, filepath=output_full_path)
                    message = 'Success'
            elif ttsselected == 'PYTTS':
                voice = request.POST.get('pyttsVoice') or 1
                vol = request.POST.get('pyttsVol') or 1.0
                rate = request.POST.get('pyttsRate') or 125
                tts = PYTTS()

                dir = 'CONVERTED_TEXT_TO_AUDIO/'+ttsselected+'/'+str(dirSub)+'/'
                createDir(dir)
                output_full_path = joinDirwithPath(dir, output_filename = 'output_audio.mp3')
                tts.run(text=text, filepath=output_full_path,voice=voice, vol=vol, rate=rate)
                message = 'Success'
        else:
            message = "No text provided for conversion."

    return render(request,'texttovoice/home.html',{'title':title, 'message':message})
    # return render(request,'texttovoice/home.html',{'title':title, 'message': message})
