# 🌐 Real-Time Voice Translator

<img width="1536" height="1024" alt="Voice Translator thumbnail" src="https://github.com/user-attachments/assets/7bb6ac4b-12b0-435b-87b3-f4c9fbe27c37" />

**Streamlit version ** — a Python application that captures speech input, translates it to a selected target language, and plays back the translated audio. This web version improves accessibility and user experience while preserving the core functionality: speech recognition → translation → text-to-speech.

---

## 🔎 Overview

Real Time Voice Translator listens to microphone input (or accepts uploaded audio), recognizes the spoken text, translates it to a chosen target language, and returns both the translated text and an audio playback of the translated text.

Key goals:
- Fast, simple user flow for live voice translation
- Multilingual support for input and output
- Continuous start/stop control for conversation flows

---

## 🧰 Technology Stack

- **Python 3.10+**
- **Streamlit** – web UI
- **SpeechRecognition** – microphone audio capture and speech→text
- **deep-translator** (GoogleTranslator) – text translation
- **gTTS** – text→speech audio generation
- **google-transliteration-api** – transliteration support for non-Latin scripts
- **SQLite** – local storage for recordings / transcripts (optional)
- **pydub / ffmpeg** – audio format conversion (if needed)

---

## ✨ Features

- Select input & output language from a predefined list.
- Live microphone capture with start/stop controls.
- Automatic speech recognition (speech → text).
- Machine translation of recognized text to the chosen target language.
- Play translated text as audio inside the web app.
- Show original recognized text and translated text in UI.
- Edit transcription before saving.
- Error handling for recognition/translation failures and friendly messages.

---

## 📁 Project Structure

/
├── app_streamlit.py # Streamlit front-end (main web app)
├── main.py # Original Tkinter app (reference)
├── requirements.txt # Python dependencies
├── README.md # This file
├── REPORT.md # Detailed project report
├── CONTRIBUTING.md # Contribution guidelines
├── CHANGELOG.md # Project changelog

---

## ▶ Installation

1. **Clone the repo**
```bash
git https://github.com/Harshal870/real-time-voice-translator
cd linguasync
```

2. **Create & activate virtual environment**
```bash
python -m venv env
# Windows
env\Scripts\activate
# macOS / Linux
source env/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

*Note (Windows users):* If pyaudio fails to install, install the appropriate wheel for your Python version or install PortAudio (or use file upload as fallback).

(Optional) If you plan to use local audio conversions, ensure ffmpeg is installed and available in PATH.

---

## ▶ Configuration

Create a `.env` file from the example and add any optional keys:

```text
# .env (create from .env.example)
# Optional: keys for cloud services if you use them
GOOGLE_API_KEY=
WHISPER_MODEL=base
DATABASE_PATH=corpus.db
```

The app is designed to work with the speech_recognition library's `recognize_google()` method (which typically works without an API key for small usage). If you prefer a paid/official Google Cloud setup, configure credentials as required.

---

## ▶ Running the App

Start Streamlit:

```bash
streamlit run app_streamlit.py
```

- Select Input Language and Output Language.
- Click Start (allow microphone access when prompted by the browser).
- Speak clearly — the app will show recognized text, translate it, then play back the translated audio.
- Edit the transcription if needed, then Save to store the record locally.

---


## ✅ Supported Languages (example)

Input and output languages can include (configurable list in `app_streamlit.py`):

- English (en)
- Hindi (hi)
- Bengali (bn)
- Spanish (es)
- Chinese (Simplified) (zh-CN)
- Russian (ru)
- Japanese (ja)
- Korean (ko)
- German (de)
- French (fr)
- Tamil (ta)
- Telugu (te)
- Kannada (kn)
- Gujarati (gu)
- Punjabi (pa)

You can expand this list by editing the languages mapping in the app.

---

## ⚠ Known Limitations

- Internet required for speech recognition and Google translation by default.
- gTTS may not support all languages or voices (some languages may fail).
- Browser-based audio playback behavior varies by browser and platform.
- Real-time performance is constrained by network latency and client CPU.
- For robust offline transcription, consider integrating Whisper (local) as a future improvement.

---

## 🛠 Troubleshooting

- Microphone not found / permission denied: ensure the browser has permission to use the microphone; try a different browser.
- pyaudio install failure (Windows): install the appropriate wheel from PyPI unofficial wheels or use file-upload fallback.
- No audio playback: check browser audio settings; try playsound fallback or download the MP3 and play externally.
- Transcription returns empty or garbage: speak clearly, increase input volume, or try a different input language code.

---

## 🔮 Future Improvements

- Add more languages & dialect-specific models.
- Add offline transcription (OpenAI Whisper / Vosk) and offline TTS options.
- Improve UI/UX with progress indicators and conversation history.
- Implement user authentication & history tracking for persistent users.
- Provide a public Hugging Face Space demo for easy sharing (if compatible).
- Add multi-speaker diarization and punctuation improvements.

---

## 🤝 Contributing

Contributions are welcome. Please follow these steps:

- Fork the repo and create a feature branch:
  ```bash
  git checkout -b feature/your-feature
  ```
- Make changes, test thoroughly.
- Commit and push your branch, then open a Merge Request.
- Update CHANGELOG.md with notable changes.
- Please read CONTRIBUTING.md for code style and commit guidelines.

---

## 🧾 License

This project is released under the AGPLv3 License — see LICENSE for details.

---

## 👥 Authors & Acknowledgements




Original idea and internship: Viswam.ai / Swecha (Summer of AI 2025)

Libraries & models: SpeechRecognition, deep-translator, gTTS, Streamlit

---

## 📺 Demo 
https://youtu.be/WB1wDMpseBg?si=eWcA9bIFdnNJYJWp

