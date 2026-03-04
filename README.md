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

## ✨ Features

| Feature | Details |
|---|---|
| 🎙️ **Transcription** | Powered by OpenAI Whisper (`base` model) with timestamped segments |
| 🤖 **AI Summarization** | Facebook BART large-CNN model condenses long audio into key points |
| 🌍 **Translation** | Translate transcript + summary into 8 languages on the fly |
| 📄 **Export** | Download results as formatted TXT or PDF (with multi-language font support) |
| 🔐 **Auth** | Register & login via **email or phone number** |
| 🔑 **Password Reset** | Secure reset link sent to registered email (30-minute expiry) |
| 💪 **Password Strength** | Live strength meter enforcing length, uppercase & special character rules |
| 📜 **History** | Browse, replay, and delete previously uploaded files |
| 🤖 **Robot Mascot** | Interactive eye-tracking bot with star-eye animation |

---


# 🧠 System Architecture

User Uploads Audio  
↓  
Flask Backend Server  
↓  
Audio Saved to Server  
↓  
Whisper AI Model  
↓  
Transcript Generated  
↓  
Translation Module  
↓  
Summarization Model  
↓  
Display Results to User  
↓  
Export as TXT or PDF  

---

# 📁 Project Structure

```
Transcribe-Flow/
│
├── app.py                  # Flask backend
├── index.html              # Frontend UI
├── get_fonts.py            # Font downloader
├── fix_font.py             # Font configuration
│
├── uploads/                # Uploaded audio files
├── outputs/                # Generated transcripts and summaries
│
├── NotoSans-Regular.ttf   # Unicode font
├── LICENSE
└── README.md
```

---

# ⚙️ Technology Stack

| Layer | Technology |
|------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask (Python) |
| AI Model | Whisper |
| NLP | HuggingFace Transformers |
| File Export | FPDF |
| Storage | Local filesystem |

---

# 🛠️ Installation & Setup

## Clone Repository

```
git clone https://github.com/Aritra-Dey2004/Transcribe-Flow.git
cd Transcribe-Flow
```

## Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows:
```
venv\Scripts\activate
```

Linux/Mac:
```
source venv/bin/activate
```

## Install Dependencies

```
pip install -r requirements.txt
```

## Run Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 📊 Example Output

Transcript:
```
Today we discussed the project timeline and milestones.
```

Summary:
```
Discussion about project planning and execution timeline.
```

---

# 🎯 Skills Demonstrated

- Python programming
- Flask backend development
- AI model integration
- Natural Language Processing
- Full-stack development
- File handling and export
- Web application architecture

---

# 👨‍💻 Author

**Aritra Dey**  
BTech Computer Science (Data Science) Student  



---

# 🔮 Future Improvements

- Speaker diarization
- Real-time transcription
- Cloud deployment
- User authentication
- Database integration

---

# 📜 License

MIT License
