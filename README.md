# 📷🗣️ Text Reader & Voice Assistant

A real-time, camera-powered text reader with multilingual OCR and voice playback. Bring text on paper to life using your webcam! Supports English 🇬🇧, Bengali 🇧🇩, Hindi 🇮🇳, and Tamil 🇮🇳.

---

## 🚀 Features

- 🎥 **Live Camera Preview** with enhanced GUI overlay  
- 👁️‍🗨️ **Instant OCR** from a smart capture area  
- 🔊 **Text-to-Speech** for extracted text  
- 🌐 **Multiple Languages:** English, Bengali, Hindi, Tamil (press 1-4)
- ⌨️ **Hotkey Controls:**  
  1️⃣ 2️⃣ 3️⃣ 4️⃣ — Change language  
  ⬜️ **SPACE** — Capture & Read Text  
  🔁 **R** — Repeat Last Text  
  ❌ **Q** — Quit Application
- 🪞 **Mirror Mode** for easy point-and-capture interface

---
## 🏁 Getting Started

### 1. Prerequisites
- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed (and on your PATH)

- ### 2. Installation
- git clone https://github.com/Rivu5555/Smart-glasses-Nav-Eye-.git
- cd TextReaderApp
  pip install -r requirements.txt
- **Tesseract Installation:**
  - 🪟 **Windows**: [Download here](https://github.com/tesseract-ocr/tesseract)
  - 🐧 **Linux**:  
    `sudo apt-get install tesseract-ocr tesseract-ocr-ben tesseract-ocr-hin tesseract-ocr-tam`
  - 🍏 **Mac**:  
    `brew install tesseract`

### 3. Recommended Settings

- Download and place language files (`ben.traineddata`, `hin.traineddata`, `tam.traineddata`) in your Tesseract `tessdata` directory for full language support.

---

## ⚡ Usage

Update the Tesseract path in `text_reader_app.py` if needed:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

## 🎛️ Controls

| Key     | Action                        | Emoji  |
|---------|-------------------------------|--------|
| 1       | Switch to English             | 🇬🇧    |
| 2       | Switch to Bengali             | 🇧🇩    |
| 3       | Switch to Hindi               | 🇮🇳    |
| 4       | Switch to Tamil               | 🇮🇳    |
| SPACE   | Capture & Read Text           | ⬜️     |
| R       | Repeat Last Text              | 🔁     |
| Q       | Quit Application              | ❌     |

---

## 📦 Dependencies

- opencv-python
- pytesseract
- pillow
- gtts
- pygame
- numpy

- Install all with:
pip install -r requirements.txt


---

## 💡 Troubleshooting

- ⚠️ *Tesseract not found?* Check path in your script!
- 🔇 *No audio?* Ensure your device’s sound is enabled and pygame is working.
- 📋 *No text detected?* Adjust camera, lighting, and ensure text is within the green box.

---

## 🙌 Contributing

Pull requests are welcome! For changes, please open an issue to discuss ideas.

---



  
