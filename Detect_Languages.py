# Detect_Languags.py

# Command install packages:
# pip install langdetect

from langdetect import detect


def translate_language(lang_code):
    languages = {
        'af': 'Afrikaans',
        'ar': 'Arabic',
        'bg': 'Bulgarian',
        'bn': 'Bengali',
        'ca': 'Catalan',
        'cs': 'Czech',
        'cy': 'Welsh',
        'da': 'Danish',
        'de': 'German',
        'el': 'Greek',
        'en': 'English',
        'es': 'Spanish',
        'et': 'Estonian',
        'fa': 'Persian',
        'fi': 'Finnish',
        'fr': 'French',
        'gu': 'Gujarati',
        'he': 'Hebrew',
        'hi': 'Hindi',
        'hr': 'Croatian',
        'hu': 'Hungarian',
        'id': 'Indonesian',
        'it': 'Italian',
        'ja': 'Japanese',
        'kn': 'Kannada',
        'ko': 'Korean',
        'lt': 'Lithuanian',
        'lv': 'Latvian',
        'mk': 'Macedonian',
        'ml': 'Malayalam',
        'mr': 'Marathi',
        'ne': 'Nepali',
        'nl': 'Dutch',
        'no': 'Norwegian',
        'pa': 'Punjabi',
        'pl': 'Polish',
        'pt': 'Portuguese',
        'ro': 'Romanian',
        'ru': 'Russian',
        'sk': 'Slovak',
        'sl': 'Slovene',
        'so': 'Somali',
        'sq': 'Albanian',
        'sv': 'Swedish',
        'sw': 'Swahili',
        'ta': 'Tamil',
        'te': 'Telugu',
        'th': 'Thai',
        'tl': 'Tagalog',
        'tr': 'Turkish',
        'uk': 'Ukrainian',
        'ur': 'Urdu',
        'vi': 'Vietnamese',
        'zh-cn': 'Chinese (Simplified)',
        'zh-tw': 'Chinese (Traditional)'
    }
    return languages.get(lang_code, "Unknown")


text = 'สวัสดีครับ my name is stamp i want to talk about हाल ही में, जेमिनी या बार्ड ने अपनी गति के लिए सोशल मीडिया का ध्यान आकर्षित किया है, लेकिन हाल ही में चैटजीपीटी के निर्माता ओपनाई ने सैम ऑल्टमैन के ट्विटर के माध्यम से हलचल मचा दी है, जिन्होंने पोस्ट किया था कि नेटिज़न्स किसी भी वाक्य पर टिप्पणी कर सकते हैं और वह सोरा को बना देंगे। वह वीडियो उसके लिए.'
detected_lang = detect(text)
language_detected = translate_language(detected_lang)

print(language_detected)
