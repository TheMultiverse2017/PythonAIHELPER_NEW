from django.http import HttpResponse
import os
from django.conf import settings

def allvoicesForTikTok():
    all_voices = [
        ['en_us_ghostface', 'Disney Voice - Ghost Face'],
        ['en_us_chewbacca', 'Disney Voice - Chewbacca'],
        ['en_us_c3po', 'Disney Voice - C3PO'],
        ['en_us_stitch', 'Disney Voice - Stitch'],
        ['en_us_stormtrooper', 'Disney Voice - Stormtrooper'],
        ['en_us_rocket', 'Disney Voice - Rocket'],
        ['en_female_madam_leota', 'Disney Voice - Madame Leota'],
        ['en_male_ghosthost', 'Disney Voice - Ghost Host'],
        ['en_male_pirate', 'Disney Voice - Pirate'],
        ['en_au_001', 'Eng Voice - English AU - Female'],
        ['en_au_002', 'Eng Voice - English AU - Male'],
        ['en_uk_001', 'Eng Voice - English UK - Male 1'],
        ['en_uk_003', 'Eng Voice - English UK - Male 2'],
        ['en_us_001', 'Eng Voice - English US - Female (Int. 1)'],
        ['en_us_002', 'Eng Voice - English US - Female (Int. 2)'],
        ['en_us_006', 'Eng Voice - English US - Male 1'],
        ['en_us_007', 'Eng Voice - English US - Male 2'],
        ['en_us_009', 'Eng Voice - English US - Male 3'],
        ['en_us_010', 'Eng Voice - English US - Male 4'],
        ['en_male_narration', 'Eng Voice - Narrator'],
        ['en_male_funny', 'Eng Voice - Funny'],
        ['en_female_emotional', 'Eng Voice - Peaceful'],
        ['en_male_cody', 'Eng Voice - Serious'],
        ['fr_001', 'Non Eng Voices - French - Male 1'],
        ['fr_002', 'Non Eng Voices - French - Male 2'],
        ['de_001', 'Non Eng Voices - German - Female'],
        ['de_002', 'Non Eng Voices - German - Male'],
        ['es_002', 'Non Eng Voices - Spanish - Male'],
        ['it_male_m18', 'Non Eng Voices - Italian - Male'],
        ['es_mx_002', 'Non Eng Voices - Spanish MX - Male'],
        ['br_001', 'Non Eng Voices - Portuguese BR - Female 1'],
        ['br_003', 'Non Eng Voices - Portuguese BR - Female 2'],
        ['br_004', 'Non Eng Voices - Portuguese BR - Female 3'],
        ['br_005', 'Non Eng Voices - Portuguese BR - Male'],
        ['id_001', 'Non Eng Voices - Indonesian - Female'],
        ['jp_001', 'Non Eng Voices - Japanese - Female 1'],
        ['jp_003', 'Non Eng Voices - Japanese - Female 2'],
        ['jp_005', 'Non Eng Voices - Japanese - Female 3'],
        ['jp_006', 'Non Eng Voices - Japanese - Male'],
        ['kr_002', 'Non Eng Voices - Korean - Male 1'],
        ['kr_003', 'Non Eng Voices - Korean - Female'],
        ['kr_004', 'Non Eng Voices - Korean - Male 2'],
        ['en_female_f08_salut_damour', 'Vocals - Alto'],
        ['en_male_m03_lobby', 'Vocals - Tenor'],
        ['en_male_m03_sunshine_soon', 'Vocals - Sunshine Soon'],
        ['en_female_f08_warmy_breeze', 'Vocals - Warmy Breeze'],
        ['en_female_ht_f08_glorious', 'Vocals - Glorious'],
        ['en_male_sing_funny_it_goes_up', 'Vocals - It Goes Up'],
        ['en_male_m2_xhxs_m03_silly', 'Vocals - Chipmunk'],
        ['en_female_ht_f08_wonderful_world', 'Vocals - Dramatic']
    ]

    return all_voices

def downloadAudio(dir):
    audio_file_path = os.path.join(settings.BASE_DIR, dir)
    try:
        with open(audio_file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename="audio_file.mp3"'
            return response
    except PermissionError:
        # Handle permission error
        return HttpResponse("Permission denied", status=403)
    except FileNotFoundError:
        # Handle file not found
        return HttpResponse("File not found", status=404)