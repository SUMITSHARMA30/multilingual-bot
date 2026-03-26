import streamlit as st
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import playsound

# 🗺️ Manual mapping Hindi to English if needed (optional)
lang_map = {
    'Bengali': 'bn',
    'Marathi': 'mr',
    'Tamil': 'ta',
    'Gujarati': 'gu',
    'Hindi': 'hi',
    'Haryanvi': 'hi',
    'English': 'en',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Telugu': 'te',
    'Kannada': 'kn',
    'Urdu': 'ur',
    'Punjabi': 'pa',
    'Sanskrit': 'sa',
    'Arabic': 'ar',
    'Chinese': 'zh-cn',
    'Japanese': 'ja',
}

# 🎤 Voice recorder
def record_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='en-IN')
            st.success(f"🗣️ You said: {text}")
            return text
        except:
            st.error("😕 Could not understand.")
            return ""

# 🔊 Convert and play audio
def speak(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code)
        filename = "output.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        st.error(f"❌ Audio playback failed: {e}")

# 🚀 Streamlit App
def main():
    st.title("🎙️ Real-time Voice Translator")

    # 🎯 Language dropdown
    target_language = st.selectbox("🌐 Choose your target language", list(lang_map.keys()))
    target_lang_code = lang_map[target_language]

    # 🔘 Start Recording
    if st.button("🎤 Start Voice Recording"):
        original_text = record_voice()
        if original_text:
            # 🌍 Translate
            translator = Translator()
            translated = translator.translate(original_text, dest=target_lang_code)
            st.success(f"🌐 Translated ({target_lang_code}): {translated.text}")
            speak(translated.text, target_lang_code)

if __name__ == "__main__":
    main()
