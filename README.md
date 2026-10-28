
# Echoes — The Memory Lantern 🕯️

**Turn meaningful memories into heartfelt keepsakes with AI-generated narration.**

Echoes is an AI-powered memory-preservation application that transforms personal memories into warm, reflective written keepsakes. Users can choose a writing style, generate a keepsake using a locally running language model, listen to an audio narration, and download the resulting text.

## ✨ Features

- **AI-generated keepsakes:** Transform personal memories into heartfelt written reflections.
- **Multiple writing styles:** Choose between warm and nostalgic, poetic and reflective, gentle and comforting, or simple and heartfelt.
- **Audio narration:** Listen to generated keepsakes using ElevenLabs text-to-speech.
- **Downloadable keepsakes:** Save your generated text for later.
- **Local AI generation:** Use Ollama with Qwen 2.5 for memory generation on your own machine.

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama
- Qwen 2.5 (1.5B)
- ElevenLabs Text-to-Speech

## 🚀 Run Locally

### Prerequisites

- Python 3.10 or a compatible version
- Ollama installed
- The `qwen2.5:1.5b` model downloaded
- An ElevenLabs API key for audio narration

### 1. Clone the repository

```bash
git clone https://github.com/sudiksha8639-debug/echoes-memory-lantern.git
cd echoes-memory-lantern
```

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit requests python-dotenv elevenlabs
```

### 4. Download the local AI model

```bash
ollama pull qwen2.5:1.5b
```

Make sure Ollama is running before launching the application.

### 5. Configure audio narration

Create a `.env` file in the project root:

```env
ELEVENLABS_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own ElevenLabs API key. Never commit your real API key to GitHub.

### 6. Launch Echoes

```bash
python -m streamlit run app.py
```

Open the local URL shown in your terminal, usually `http://localhost:8501`.

## 🔐 Privacy and Security

- Keep API keys in environment variables rather than source code.
- The `.env` file is excluded from Git through `.gitignore`.
- Local AI generation requires Ollama to be running on your machine.

## 🌱 Future Improvements

- Deploy a publicly accessible version.
- Add more keepsake styles and personalization options.
- Explore additional ways to organize and revisit saved memories.

## 👩‍💻 Author

Created by **Sudiksha Das**.

---

*Every memory holds a story worth keeping.*
