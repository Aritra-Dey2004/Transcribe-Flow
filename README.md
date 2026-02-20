# 🎧 TranscribeFlow
### AI Audio Transcription, Translation & Summarization Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![AI](https://img.shields.io/badge/AI-Whisper-green?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Transformers-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</p>

---

# 🚀 Project Overview

TranscribeFlow is an AI-powered full-stack web application that converts audio into text, translates it into English, and generates intelligent summaries automatically.

This project demonstrates practical implementation of:

- Automatic Speech Recognition (ASR)
- Natural Language Processing (NLP)
- Full-Stack Web Development
- AI Model Integration in Production Systems

---

# ✨ Key Features

🎙️ Audio Transcription  
- Converts audio (.mp3, .wav) → text  
- Powered by Whisper AI model  

🌍 Translation Support  
- Multilingual transcription  
- Automatic English translation  

🧠 AI Summarization  
- Generates concise summaries  
- Uses Transformer NLP models  

📄 Export Options  
- Download transcript as TXT  
- Download transcript as PDF  
- Unicode font support  

⏱️ Timestamp Support  
- Timestamped transcription  
- Easy content navigation  

🌐 Web Interface  
- Clean and responsive UI  
- Real-time processing  

---

# 🧠 System Architecture

```mermaid
flowchart TD

A[User Uploads Audio] --> B[Flask Backend]
B --> C[Whisper AI Model]
C --> D[Transcript Generated]
D --> E[Translation Module]
E --> F[Summarization Model]
F --> G[Results Displayed]
G --> H[Export TXT/PDF]
