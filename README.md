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

A[User Uploads Audio File] --> B[Flask Backend Server]

B --> C[Audio Saved Locally]

C --> D[Whisper AI Model]

D --> E[Transcript Generated]

E --> F[Translation Module]

F --> G[Summarization Model]

G --> H[Display Results to User]

H --> I[Export as TXT or PDF]
Transcribe-Flow/
│
├── app.py                     # Flask backend
├── index.html                 # Frontend UI
├── get_fonts.py              # Font downloader
├── fix_font.py               # Font configuration
│
├── uploads/                  # Uploaded audio files
├── outputs/                  # Generated files
│
├── NotoSans-Regular.ttf     # Unicode font support
├── LICENSE
└── README.md
⚙️ Technology Stack
Layer	Technology
Frontend	HTML, CSS, JavaScript
Backend	Flask (Python)
AI Model	Whisper
NLP	HuggingFace Transformers
File Export	FPDF
Storage	Local filesystem
🛠️ Installation & Setup
Clone Repository
git clone https://github.com/Aritra-Dey2004/Transcribe-Flow.git
cd Transcribe-Flow
Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run Application
python app.py

Open browser:

http://127.0.0.1:5000
📊 Example Output

Transcript:

Today we discussed the project timeline and milestones.

Summary:

Discussion about project planning and execution timeline.
🎯 Skills Demonstrated

This project demonstrates proficiency in:

Python development

Flask backend development

AI model integration

Natural Language Processing

File handling

Web application architecture

Real-world AI deployment
