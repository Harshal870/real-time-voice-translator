# System Architecture & Technical Structure

The **Real-Time Voice Translator** follows a modular, layer-based architecture that separates input handling, speech processing, translation, audio synthesis, and user interface components.

---

## Tech Stack Overview

| Layer | Technology |
| :--- | :--- |
| **Frontend Framework** | Streamlit (Python Web UI) |
| **Audio Capture** | HTML5 Web Audio API (`st.audio_input`) |
| **Speech-to-Text (ASR)** | SpeechRecognition (Google Web Speech API) |
| **Translation Engine** | `deep-translator` (Google Translate API) |
| **Text-to-Speech (TTS)** | `gTTS` (Google Text-to-Speech) |
| **System Dependencies** | Linux `portaudio19-dev`, `ffmpeg` |
| **Cloud Hosting** | Streamlit Community Cloud |

---

## High-Level Data Flow

```text
[ User Microphone ]
       │ (Browser HTML5 Audio Capture)
       ▼
[ st.audio_input Buffer ]
       │ (WAV / Audio Memory Stream)
       ▼
[ SpeechRecognition Engine ] ──► (Google Web Speech API)
       │
       ▼ (Recognized Text)
[ Transliteration Layer ] (Optional non-Latin script processing)
       │
       ▼
[ Deep Translator ] ──► (Google Translate API)
       │
       ▼ (Translated Text)
┌──────┴──────────────────────────┐
│                                 │
▼                                 ▼
[ Text-to-Speech (gTTS) ]    [ CSV Data Buffer ]
│                            │
▼                            ▼
[ In-Browser Audio Player ]  [ Download Button ]
