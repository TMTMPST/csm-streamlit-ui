# 🎙️ CSM AI - Streamlit UI

## 🌟 Overview
Welcome to the **CSM AI - Streamlit UI**, a user-friendly interface for the **CSM AI text-to-speech generator** powered by deep learning. This project enables users to:
- **Upload** audio files for training
- **Input text** to generate high-quality speech
- **Preview and download** generated audio

## 🚀 Features
✔️ **Audio Upload:** Supports MP3, WAV, and FLAC formats, stored in the `/data` folder  
✔️ **Preview Audio:** Listen to uploaded files before processing  
✔️ **Text-to-Speech Generation:** Convert text into speech using the **CSM AI model**  
✔️ **Download Audio:** Get the output in WAV format  
✔️ **Modern UI:** Interactive and easy-to-use **Streamlit interface** with custom styling  

## 📂 Project Structure
```
csm-streamlit-ui/
│── streamlit_app/
│   │── app.py  # Main Streamlit UI script
│   ├── assets/
│   │   ├── styles.css  # Custom styling (optional)
│   ├── data/  # Stores uploaded and generated audio files
│
│── models/
│   │── models.py  # Model definitions
│
│── generator/
│   │── generator.py  # Text-to-speech logic
│   │── test_clone.py  # Runs the AI model
│
│── requirements.txt  # Dependencies
│── setup.py  # Project setup file
│── run_csm.py  # Script to start the model
│── README.md  # Documentation
│── venv/  # Virtual environment (optional)
```

## 🛠️ Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/csm-streamlit-ui.git
cd csm-streamlit-ui
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```sh
streamlit run streamlit_app/app.py
```

## 🎧 How to Use
1. **Upload an audio file** (MP3, WAV, or FLAC) to the system for training.  
2. **Enter text** in the provided input box.  
3. Click **"Generate Audio"** to synthesize speech.  
4. **Preview and download** the generated audio.  

## ⚡ Technologies Used
🔹 **Streamlit** – Frontend UI for interaction  
🔹 **PyTorch** – Deep learning framework  
🔹 **Torchaudio** – Audio processing library  
🔹 **CSM AI** – The core text-to-speech engine  

## 📜 License
This project is licensed under the **Apache 2.0 License**.

## 🏆 Credits
Developed by **Vidi Joshubzky Saviola** 🚀

## 🔗 Original Repository
This project is based on the original CSM AI implementation:
[CSM AI GitHub](https://github.com/SesameAILabs/csm)

