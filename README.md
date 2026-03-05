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

## 🖥️ Tech Stack

**Backend**
- [Flask](https://flask.palletsprojects.com/) — web framework
- [OpenAI Whisper](https://github.com/openai/whisper) — speech-to-text
- [HuggingFace Transformers](https://huggingface.co/facebook/bart-large-cnn) — BART summarization
- [deep-translator](https://github.com/nidhaloff/deep-translator) — Google Translate wrapper
- [FPDF2](https://py-fpdf2.readthedocs.io/) — PDF generation
- [PassLib + Argon2](https://passlib.readthedocs.io/) — password hashing
- [PyJWT](https://pyjwt.readthedocs.io/) — JWT authentication tokens
- [python-dotenv](https://github.com/theskumar/python-dotenv) — environment variable management

**Frontend**
- Vanilla HTML / CSS / JavaScript
- [Vanta.js](https://www.vantajs.com/) — animated wave background
- [SweetAlert2](https://sweetalert2.github.io/) — styled modals & alerts

**Storage**
- `users.json` — lightweight file-based user database
- `uploads/` — local folder for audio + transcript files

---

# 🛠️ Installation & Setup

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/transcribeflow.git
cd TranscribeFlow
```

### 2. Create & activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** Whisper also requires [ffmpeg](https://ffmpeg.org/download.html) to be installed on your system.
> - **Windows:** `winget install ffmpeg` or download from the website
> - **macOS:** `brew install ffmpeg`
> - **Linux:** `sudo apt install ffmpeg`

### 4. Set up environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and edit:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_16_char_app_password
SMTP_FROM=your_email@gmail.com
APP_BASE_URL=http://127.0.0.1:5000
```

> **Gmail setup:** Go to **Google Account → Security → 2-Step Verification → App Passwords** and generate a 16-character app password. Use that as `SMTP_PASSWORD` — never your actual Gmail password.

### 5. Run the app

```bash
python app.py
```

Visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

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
## 🌍 Supported Translation Languages

| Language | Code |
|---|---|
| English | `en` |
| Hindi | `hi` |
| Spanish | `es` |
| French | `fr` |
| German | `de` |
| Chinese (Simplified) | `zh-CN` |
| Japanese | `ja` |
| Arabic | `ar` |

---

## 🔐 Authentication

### Register
- Requires name, email, and password
- Phone number is optional — but once added, you can log in with it
- Password must have: ≥ 8 characters, 1 uppercase letter, 1 special character

### Login
- Toggle between **Email** and **Phone** login in the modal
- JWT token stored in `localStorage` (6-hour expiry)

### Forgot Password
1. Click "Forgot your password?" in the login modal
2. Enter your registered email
3. Check your inbox for a reset link (valid for 30 minutes)
4. Set a new password that meets the strength requirements

---

## ⚙️ Configuration Reference

| Variable | Description | Default |
|---|---|---|
| `SMTP_HOST` | SMTP server address | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP port | `587` |
| `SMTP_USER` | Your email address | — |
| `SMTP_PASSWORD` | App password (not your login password) | — |
| `SMTP_FROM` | Sender address shown in email | Same as `SMTP_USER` |
| `APP_BASE_URL` | Base URL for reset links | `http://127.0.0.1:5000` |

---

## 🔒 Security Notes

- Passwords are hashed with **Argon2** (resistant to brute-force attacks)
- Password reset tokens are single-use and expire after 30 minutes
- JWT tokens expire after 6 hours
- Never commit your `.env` file — it is listed in `.gitignore`
- The `users.json` file contains hashed passwords — also excluded from git


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
## 🙋 FAQ

**Q: The app loads but transcription never completes.**
A: Make sure `ffmpeg` is installed and accessible in your system PATH.

**Q: I'm not receiving the password reset email.**
A: Double-check your `SMTP_PASSWORD` is a Gmail App Password (not your account password), and that 2-Step Verification is enabled on your Google account.

**Q: Can I use a different email provider?**
A: Yes — update `SMTP_HOST` and `SMTP_PORT` in your `.env` to match your provider (e.g. Outlook uses `smtp.office365.com` on port `587`).

**Q: The BART model takes a long time to load.**
A: The model (~1.6 GB) is loaded into memory at startup. This is a one-time cost per server restart. Consider running on a machine with at least 4 GB RAM.

**Q: How do I deploy this to production?**
A: Use a WSGI server like **Gunicorn** behind **Nginx**, set `APP_BASE_URL` to your domain in `.env`, and use HTTPS so that reset links are secure.

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

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  <strong>Built with ❤️ using Flask + Whisper + BART</strong>
</div>
