import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import uuid
import os
import playsound


# Voice to text
def record_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("🎤 Listening..."):
            audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return "Could not understand audio"


# Translate the input
def translate_text(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text


# Speak the translated text
def speak_text(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = f"temp_{uuid.uuid4().hex}.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


# 🌐 Language code map
language_map = {
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
    'Bhojpuri': 'bho'  # Added Bhojpuri
}



# 🚀 Streamlit UI starts here
st.set_page_config(page_title="Multilingual Voice Translator", page_icon="🌍", layout="centered")

st.markdown(
    """
    <style>
        .main {
            background-color: #f0f2f6;
            color: #1c1c1e;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center;
            color: #0072ff;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton button {
            background-color: #0072ff;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 0.5rem 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("# 🌐SUMIT's Language Translator Bot ")
st.markdown("### 🔊 Speak → 🧠 Translate → 🗣️ Speak Back")

# UI Inputs
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("🎙️ Select Source Language", list(language_map.keys()), index=1)
with col2:
    target_lang = st.selectbox("🗣️ Select Target Language", list(language_map.keys()), index=0)

if st.button("🎤 Start Recording"):
    input_text = record_voice()
    st.text_area("🔍 You Said:", input_text, height=100)

    # Translate & Speak
    translated_text = translate_text(input_text, dest_language=language_map[target_lang])
    st.success(f"📘 Translated ({target_lang}): {translated_text}")
    
    speak_text(translated_text, lang=language_map[target_lang])
st.markdown(
    """
    <style>
        /* === Background Gradient === */
        .main {
            background: linear-gradient(to bottom right, #fffde4, #fbd786);
            font-family: 'Segoe UI', sans-serif;
            color: #1c1c1e;
        }

        /* === Header === */
        h1 {
            text-align: center;
            font-size: 2.8rem;
            color: #000000; /* Bold black title */
            font-weight: 800;
        }

        h3 {
            text-align: center;
            color: #333;
            font-weight: 500;
            margin-bottom: 30px;
        }

        /* === Container Styling === */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 750px;
            margin: auto;
            background-color: #ffffffcc;
            border-radius: 20px;
            box-shadow: 0 4px 30px rgba(0,0,0,0.1);
            padding: 2rem;
        }

        /* === Buttons === */
        .stButton button {
            background: linear-gradient(90deg, #ffcc00, #ff9900);
            color: #000;
            font-weight: bold;
            border-radius: 12px;
            padding: 0.7rem 1.6rem;
            font-size: 16px;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        .stButton button:hover {
            background: linear-gradient(90deg, #ffdd33, #ffaa33);
        }

        /* === Dropdowns === */
        .stSelectbox label {
            font-weight: 600;
            color: #222;
        }

        /* === Text Area === */
        textarea {
            border-radius: 10px !important;
            font-size: 16px !important;
            color: #333 !important;
            background-color: #fefefe !important;
        }

        /* === Success alert === */
        .stAlert-success {
            background-color: #e7fbe9;
            border-left: 5px solid #34a853;
        }

        /* === Animated Voice Wave === */
        @keyframes wave {
            0% { transform: scaleY(1); }
            50% { transform: scaleY(2); }
            100% { transform: scaleY(1); }
        }

        .wave {
            display: flex;
            justify-content: center;
            gap: 6px;
            margin: 20px auto;
        }

        .wave div {
            width: 6px;
            height: 20px;
            background: #ff9900;
            animation: wave 1s infinite ease-in-out;
        }

        .wave div:nth-child(2) {
            animation-delay: 0.1s;
        }

        .wave div:nth-child(3) {
            animation-delay: 0.2s;
        }

        .wave div:nth-child(4) {
            animation-delay: 0.3s;
        }

        .wave div:nth-child(5) {
            animation-delay: 0.4s;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
    body {
        background-color: #87CEEB;
        color: black;
    }

    .stApp {
        background: linear-gradient(to bottom right, #87CEEB, #ffffff);
        padding: 20px;
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3, h4, h5, h6, p, label {
        color: black !important;
        font-weight: bold;
    }

    .css-1cpxqw2 {
        color: black !important;
    }

    .stButton > button {
        background-color: #FFA500;
        color: white !important;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 12px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #ff8c00;
    }

    .stTextInput > div > div > input {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)
