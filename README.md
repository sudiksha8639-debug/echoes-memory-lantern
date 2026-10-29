# Echoes — The Memory Lantern 🕯️

**Turn meaningful memories into heartfelt keepsakes with AI-generated writing and voice narration.**

Echoes is an AI-powered web application that transforms personal memories into warm, reflective written keepsakes. Choose a writing style, generate a personalized reflection, listen to it through AI-powered narration, and download your keepsake to preserve it.

🔗 **Live Demo:** [Open Echoes](https://the-memory-lantern.streamlit.app/)

## ✨ Features

- **AI-generated keepsakes:** Transform personal memories into thoughtful, reflective writing.
- **Multiple writing styles:** Choose Warm and Nostalgic, Poetic and Reflective, Gentle and Comforting, or Simple and Heartfelt.
- **AI voice narration:** Convert generated keepsakes into audio using ElevenLabs Text-to-Speech.
- **Free browser narration:** Listen using your browser's built-in speech synthesis as an alternative.
- **Downloadable keepsakes:** Download your generated text and, when available, narrated audio.
- **Interactive web interface:** Create and experience your keepsakes through a Streamlit application.

## 🛠️ Tech Stack

- **Python** — Application logic
- **Streamlit** — Web interface
- **Groq API** — AI-powered memory generation
- **ElevenLabs API** — Text-to-speech narration
- **Browser Speech Synthesis API** — Free browser-based narration
- **python-dotenv** — Local environment configuration

## 🚀 Run Locally

### Prerequisites

- Python 3.10 or later, preferably Python 3.12
- A Groq API key
- An ElevenLabs API key for AI audio narration

### 1. Clone the repository

```bash
git clone https://github.com/sudiksha8639-debug/echoes-memory-lantern.git
cd echoes-memory-lantern
```

### 2. Create and activate a virtual environment

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

Replace the placeholder values with your own API keys. Never commit real API keys to GitHub.

### 5. Launch Echoes

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🔐 Privacy and Security

- API keys should be stored in environment variables or deployment secrets, never in source code.
- The `.env` file is excluded from version control through `.gitignore`.
- Memories are sent to the configured AI provider for generation. Avoid entering sensitive personal information unless you are comfortable sharing it with that service.
- Audio narration availability depends on the configured ElevenLabs account and its available quota.
- Browser narration provides an alternative when AI audio narration is unavailable.

## 🌱 Future Improvements

- Add an option to organize and revisit saved keepsakes.
- Explore additional narration voices and personalization options.
- Introduce optional, privacy-conscious memory storage.

## 👩‍💻 Author

**Sudiksha Das**

---

*Every memory holds a story worth keeping.*
