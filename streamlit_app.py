import os
import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import csv
import datetime
from io import StringIO

# Try importing transliteration safely
try:
    from google.transliteration import transliterate_text
    HAS_TRANSLITERATION = True
except ImportError:
    HAS_TRANSLITERATION = False

# Dictionary of language names and codes
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-CN",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "German": "de",
    "French": "fr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Punjabi": "pa",
}

st.set_page_config(page_title="Real-Time Voice Translator", page_icon="🎙️")
st.title("Real-Time Voice🎙️ Translator🔊")

# Language selection side-by-side
col1, col2 = st.columns(2)
with col1:
    input_lang_name = st.selectbox(
        "Select Input Language:", list(language_codes.keys()), index=0
    )
with col2:
    output_lang_name = st.selectbox(
        "Select Output Language:", list(language_codes.keys()), index=1
    )

input_lang_code = language_codes[input_lang_name]
output_lang_code = language_codes[output_lang_name]

# Initialize Session State
if "current_recognized" not in st.session_state:
    st.session_state.current_recognized = ""

if "current_translated" not in st.session_state:
    st.session_state.current_translated = ""

st.markdown("---")
st.subheader("1. Record Your Voice")

# Browser-native microphone input (Works on Streamlit Cloud & Mobile)
audio_value = st.audio_input("Click the mic to speak")

if audio_value is not None:
    r = sr.Recognizer()
    try:
        # Read the recorded audio file buffer from the browser
        with sr.AudioFile(audio_value) as source:
            audio_data = r.record(source)
        
        # Perform speech recognition
        speech_text = r.recognize_google(audio_data, language=input_lang_code)
        
        # Optional transliteration if applicable
        if HAS_TRANSLITERATION and input_lang_code not in ("auto", "en"):
            try:
                speech_text = transliterate_text(speech_text, lang_code=input_lang_code)
            except Exception:
                pass  # Fallback to speech_text if transliteration API fails
        
        st.session_state.current_recognized = speech_text

        # Translate text using GoogleTranslator
        translated_text = GoogleTranslator(
            source=input_lang_code, target=output_lang_code
        ).translate(text=speech_text)
        
        st.session_state.current_translated = translated_text

    except sr.UnknownValueError:
        st.error("Could not understand the audio. Please speak clearly and try again.")
    except sr.RequestError as e:
        st.error(f"Speech Recognition service error: {e}")
    except Exception as e:
        st.error(f"Translation Error: {e}")

# Display Recognized and Translated Text (Editable)
if st.session_state.current_recognized or st.session_state.current_translated:
    st.markdown("---")
    st.subheader("2. Results & Audio Playback")

    recognized_text = st.text_area(
        "Recognized Text ⮯", 
        value=st.session_state.current_recognized, 
        height=100
    )
    st.session_state.current_recognized = recognized_text

    translated_text_editable = st.text_area(
        "Translated Text ⮯", 
        value=st.session_state.current_translated, 
        height=100
    )
    st.session_state.current_translated = translated_text_editable

    # Text-to-Speech Audio Output
    if translated_text_editable.strip():
        try:
            voice = gTTS(translated_text_editable, lang=output_lang_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                voice.save(tmp_file.name)
                audio_bytes = open(tmp_file.name, "rb").read()
            st.audio(audio_bytes, format="audio/mp3")
            os.remove(tmp_file.name)
        except Exception as e:
            st.warning(f"Could not generate audio output: {e}")

    # CSV Export Button (Downloads directly to the user's device)
    st.markdown("---")
    csv_buffer = StringIO()
    writer = csv.DictWriter(
        csv_buffer,
        fieldnames=["timestamp", "input_lang", "output_lang", "recognized_text", "translated_text"]
    )
    writer.writeheader()
    writer.writerow({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input_lang": input_lang_name,
        "output_lang": output_lang_name,
        "recognized_text": st.session_state.current_recognized,
        "translated_text": st.session_state.current_translated,
    })
    
    st.download_button(
        label="📥 Download CSV Export",
        data=csv_buffer.getvalue(),
        file_name=f"translation_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )
