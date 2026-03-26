import streamlit as st
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import playsound

# 📌 Function to record voice
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
        except sr.UnknownValueError:
            st.error("😕 Could not understand.")
            return ""
        except sr.RequestError as e:
            st.error(f"⚠️ API error: {e}")
            return ""

# 🎧 Function to speak text
def speak(text, lang_code='en'):
    try:
        tts = gTTS(text=text, lang=lang_code)
        filename = "output.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        st.error(f"❌ Audio error: {e}")

# 🌐 Get language code from name
def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return 'en'

# 🚀 Streamlit UI
def main():
    st.title("🌍 Real-Time Voice Translator Bot")
    st.write("🎙️ Speak something and choose the language to translate.")

    # Dropdown to select output language
    lang_options = list(LANGUAGES.values())
    selected_lang = st.selectbox("🌐 Select target language", sorted(lang_options))
    target_lang_code = get_language_code(selected_lang)

    # Record and translate
    if st.button("🎤 Start Recording"):
        user_text = record_voice()
        if user_text:
            translator = Translator()
            translated = translator.translate(user_text, dest=target_lang_code)
            st.write(f"🌐 Translated to {selected_lang}: **{translated.text}**")

            # Speak the translated text
            speak(translated.text, target_lang_code)

if __name__ == "__main__":
    main()
