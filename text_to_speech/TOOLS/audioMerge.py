from pydub import AudioSegment
import os
from django.conf import settings
import random


def merge_audio_files(directory):
    dir =random.randint(1,1000)
    # Create the final output directory if it doesn't exist
    final_dir = os.path.join(settings.BASE_DIR, 'CONVERTED_TEXT_TO_AUDIO/tiktok/', str(dir), 'FINAL')
    os.makedirs(final_dir, exist_ok=True)

    output_filename = 'tiktok_audio_final.mp3'
    audio_files = [file for file in os.listdir(directory) if file.endswith('.mp3')]
    combined_audio = AudioSegment.empty()

    for file in audio_files:
        audio = AudioSegment.from_file(os.path.join(directory, file), format="mp3")
        combined_audio += audio

    # Export the combined audio to the final directory
    output_path = os.path.join(final_dir, output_filename)
    combined_audio.export(output_path, format="mp3")
