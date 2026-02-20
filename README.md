# 🎧 TranscribeFlow
### AI Audio Transcription, Translation & Summarization Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![AI](https://img.shields.io/badge/AI-Whisper-green?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Transformers-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</p>

---

# 🚀 Overview

TranscribeFlow is an AI-powered web application that converts audio into text, translates it into English, and generates intelligent summaries automatically.

This project demonstrates real-world implementation of:

- Automatic Speech Recognition (ASR)
- Natural Language Processing (NLP)
- Full Stack Web Development
- AI Model Integration

---

# ✨ Features

- 🎙️ Audio transcription using Whisper AI
- 🌍 Multilingual transcription and English translation
- 🧠 Automatic AI-powered summarization
- 📄 Export transcript as TXT and PDF
- ⏱️ Timestamp support
- 🌐 User-friendly web interface
- 💾 Local file storage

---

# 🧠 System Architecture

```mermaid
flowchart TD

A[User Uploads Audio File] --> B[Flask Backend Server]

B --> C[Audio Saved to Server]

C --> D[Whisper AI Model]

D --> E[Transcript Generated]

E --> F[Translation Module]

F --> G[Summarization Model]

G --> H[Display Results to User]

H --> I[Export as TXT or PDF]
📁 Project Structure

