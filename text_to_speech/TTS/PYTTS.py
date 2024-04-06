import random
# from django.http import HttpResponse
import pyttsx3


class PYTTS:
    def __init__(self):
        self.max_chars = 5000

    def run(
        self,
        text: str,
        filepath: str,
        voice :int,
        vol :float,
        rate :int
    ):
        voice = int(voice)
        vol = float(vol)
        rate = int(rate)

        # if voice_id == "" or voice_num == "":
        #     voice_id = 2
        #     voice_num = 3
        #     raise ValueError("set pyttsx values to a valid value, switching to defaults")
        # else:
        #     voice_id = int(voice_id)
        #     voice_num = int(voice_num)
        # for i in range(voice_num):
        #     self.voices.append(i)
        #     i = +1
        # if random_voice:
        #     voice_id = self.randomvoice()

        engine = pyttsx3.init()

        """ RATE"""
        # rate = engine.getProperty('rate')   # getting details of current speaking rate
        engine.setProperty('rate', rate)     # setting up new voice rate


        """VOLUME"""
        # volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
        engine.setProperty('volume', vol  )    # setting up volume level  between 0 and 1

        voices = engine.getProperty('voices')
        engine.setProperty("voice", voices[voice].id)  # changing index changes voices but ony 0 and 1 are working here

        engine.save_to_file(text, f"{filepath}")
        engine.runAndWait()

    def randomvoice(self):
        return random.choice(self.voices)
