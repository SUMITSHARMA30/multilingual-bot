import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import playsound
import os

# 🗺️ Optional Hindi to English mapping for common languages
hindi_to_english_lang_map = {
    'बंगाली': 'bengali',
    'मराठी': 'marathi',
    'तमिल': 'tamil',
    'गुजराती': 'gujarati',
    'हिंदी': 'hindi',
    'हरियाणवी': 'haryanvi',
    'अंग्रेजी': 'english',
    'फ्रेंच': 'french',
    'स्पेनिश': 'spanish',
    'जर्मन': 'german',
    'तेलुगू': 'telugu',
    'कन्नड़': 'kannada',
    'उर्दू': 'urdu',
    'पंजाबी': 'punjabi',
    'संस्कृत': 'sanskrit',
    'अरबी': 'arabic',
    'चीनी': 'chinese',
    'जापानी': 'japanese',
}

# 🎤 Record voice and return recognized text
def record_voice(prompt_text="🎤 Speak now...", lang='hi-IN'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt_text)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language=lang)
            print("🗣️ You said:", text)
            return text
        except sr.UnknownValueError:
            print("😕 Couldn't understand.")
            return ""
        except sr.RequestError as e:
            print(f"⚠️ API error: {e}")
            return ""

# 🗣️ Convert text to speech and play it
def speak(text, lang_code='en'):
    try:
        tts = gTTS(text=text, lang=lang_code)
        filename = "output.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("❌ Could not play audio:", e)

# 🌍 Get language code from spoken language
def get_language_code(spoken_language):
    spoken_language = spoken_language.lower().strip()
    if spoken_language in hindi_to_english_lang_map:
        spoken_language = hindi_to_english_lang_map[spoken_language]

    for code, name in LANGUAGES.items():
        if spoken_language in name.lower():
            return code
    print("⚠️ Language not found, defaulting to English.")
    return 'en'  # Default fallback

# 🚀 Main program
def main():
    translator = Translator()

    # Step 1: Get user input in Hindi
    original_text = record_voice("🎤 Speak something...", lang='en-IN')

    if original_text:
        # Step 2: Ask for target language
        speak("Which language do you want to convert this to?", 'en')
        spoken_language = record_voice("🎯 Say your target language (like Bengali, Tamil, French)...", lang='hi-IN')

        # Step 3: Find target language code
        target_lang_code = get_language_code(spoken_language)

        # Step 4: Translate the text
        translated = translator.translate(original_text, dest=target_lang_code)
        print(f"🌐 Translated ({target_lang_code}):", translated.text)

        # Step 5: Speak translated output
        speak(translated.text, target_lang_code)

if __name__ == "__main__":
    main()
