# Project Features & Capabilities

The **Real-Time Voice Translator** is a web-based, cloud-ready translation application designed to bridge language barriers through instant voice recognition, machine translation, and text-to-speech audio synthesis.

## Core Features

### 🎙️ Browser-Native Voice Capture
- **Cross-Platform Recording:** Uses HTML5 audio capture (`st.audio_input`) directly in the user's web browser.
- **Hardware Agnostic:** Works seamlessly on desktop computers, tablets, and smartphones without requiring local server microphone drivers (PyAudio/ALSA).

### 🌐 Multilingual Translation
- **15+ Supported Languages:** Enables speech translation across major global and regional languages including English, Hindi, Bengali, Spanish, Chinese (Simplified), Russian, Japanese, Korean, German, French, Tamil, Telugu, Kannada, Gujarati, and Punjabi.
- **Script Transliteration:** Integrated transliteration capabilities for non-Latin scripts (e.g., converting Devnagari script input to readable text).

### ✏️ Interactive Text Editing & Verification
- **Dual Text Panels:** Displays recognized speech (source) and translated output (target) side-by-side or sequentially.
- **Editable Fields:** Allows users to manually refine or correct recognized text before audio generation if speech recognition misinterprets a word.

### 🔊 Text-to-Speech (TTS) Synthesis
- **Natural Audio Playback:** Automatically converts translated text into spoken audio using Google Text-to-Speech (`gTTS`).
- **In-Browser Audio Player:** Plays synthesized translations directly in the user interface.

### 📥 One-Click Data Export
- **Session History Logging:** Captures timestamps, source language, target language, recognized text, and translated text.
- **Direct CSV Download:** Generates a downloadable CSV file (`st.download_button`) directly to the user's local device without relying on server disk storage.

---
