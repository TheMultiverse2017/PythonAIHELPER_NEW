
import os
from django.conf import settings


def createDir(dir):
    # Specify the output directory and filename
    output_directory = os.path.join(settings.BASE_DIR, dir)

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

def joinDirwithPath(output_directory, output_filename='output_audio.mp3'):
    # Create the full output path
    output_full_path = os.path.join(output_directory, output_filename)

    return output_full_path
