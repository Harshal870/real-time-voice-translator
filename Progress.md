# Development Process & Progress Log

## Development Lifecycle Overview
The project started as a local desktop translation tool using PyAudio and Tkinter/local terminal scripts. It was refactored and transformed into a cloud-native web application deployed on Streamlit Cloud to make it globally accessible across all device types.

---

## What Went Right
- **Successful Cloud Migration:** Transitioned from hardware-bound PyAudio scripts to browser-native web audio APIs.
- **Modular Integration:** Combined `SpeechRecognition`, `deep-translator`, and `gTTS` into a single reactive Python application pipeline.
- **Export Modernization:** Upgraded local CSV writing routines to client-side streaming downloads, ensuring full compatibility with ephemeral cloud file systems.

---

## Major Technical Challenges & Resolved Bugs

### 1. Cloud Server Hardware Microphone Error (`OSError: No Default Input Device`)
- **Issue:** Running `speech_recognition.Microphone()` on Streamlit Cloud caused server crashes because cloud virtual machines lack physical microphone hardware.
- **Resolution:** Replaced `sr.Microphone()` with Streamlit's `st.audio_input` widget, passing recorded browser audio buffers into `sr.AudioFile()`.

### 2. Streamlit Cloud Package Build Crashes (`pyproject.toml` / `uv` Errors)
- **Issue:** Streamlit Cloud's build manager (`uv`) crashed due to an outdated `pyproject.toml` layout and an invalid `uv.lock` placeholder file.
- **Resolution:** Sanitized `pyproject.toml` to standard PEP 621 specifications, removed `uv.lock`, and added a `packages.txt` file containing required Linux C-libraries (`portaudio19-dev`, `python3-pyaudio`, `ffmpeg`).

### 3. File System Read/Write Restrictions on Cloud Servers
- **Issue:** Writing CSV export logs directly to local disk paths (`exports/`) was unreliable on cloud environments.
- **Resolution:** Refactored export logic to stream CSV content in-memory using `io.StringIO` via `st.download_button`.

---

## Future Enhancements & Remaining Tasks
- [ ] **Streaming Speech Recognition:** Implement WebRTC (`streamlit-mic-recorder`) for continuous real-time audio streaming.
- [ ] **Auto Language Identification:** Add automatic source language detection.
- [ ] **Custom Pronunciation & Speed Control:** Add slider controls for TTS playback speed.
- [ ] **Noise Suppression Filter:** Add client-side audio noise reduction prior to API submission.

---
