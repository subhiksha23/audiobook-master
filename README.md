# 📘 PDF to Audiobook Converter using Python 🗣️

This is a simple and efficient Python project that converts the text content of PDF files into spoken audio using Text-to-Speech (TTS) technology. It is particularly useful for visually impaired users, multitaskers, or anyone who prefers listening to content rather than reading.

---

## 🎯 Features

- ✅ Extracts text from PDF files (supports multi-page documents)
- ✅ Converts text to speech using `pyttsx3` (offline) or `gTTS` (online)
- ✅ Saves the output as an `.mp3` audio file
- ✅ Lightweight, beginner-friendly, and easy to use
- ✅ Optional GUI support using `tkinter`

---

## 🛠️ Technologies Used

- [`PyPDF2`](https://pypi.org/project/PyPDF2/) / [`pdfplumber`](https://pypi.org/project/pdfplumber/) – for PDF text extraction
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) – for offline TTS
- [`gTTS`](https://pypi.org/project/gTTS/) – for online TTS using Google Text-to-Speech
- [`tkinter`](https://docs.python.org/3/library/tkinter.html) (optional) – for GUI (if implemented)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/pdf-to-audiobook.git
cd pdf-to-audiobook
