
import os
import requests
import streamlit as st
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from groq import Groq

load_dotenv()


def get_secret(key):
    value = os.getenv(key)
    if value:
        return value

    try:
        value = st.secrets.get(key)
        if value:
            return value
    except Exception:
        pass

    return None


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Echoes | The Memory Lantern",
    page_icon="🕯️",
    layout="centered",
)

# ---------------- DESIGN ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(160deg, #17130f 0%, #211a16 55%, #302019 100%);
    color: #f5ead9;
}

.block-container {
    max-width: 820px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: 'Playfair Display', Georgia, serif !important;
    color: #f4d7a1 !important;
}

p, label, .stMarkdown, .stCaption,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label {
    font-family: 'DM Sans', sans-serif !important;
}

/* Make all form labels clearly visible */
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] *,
.stTextArea label,
.stTextInput label,
.stSelectbox label {
    color: #e8d5ba !important;
    opacity: 1 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

/* Placeholder text */
.stTextArea textarea::placeholder,
.stTextInput input::placeholder {
    color: #b8a795 !important;
    opacity: 1 !important;
}

/* Hero */
.eyebrow {
    color: #d8a85f;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-size: 11px;
    text-align: center;
}

.hero {
    text-align: center;
    padding: 1.5rem 0 1rem;
}

.hero-icon {
    font-size: 44px;
    margin-bottom: 8px;
}

.hero-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(42px, 8vw, 66px);
    color: #f4d7a1;
    line-height: 1.1;
}

.hero-subtitle {
    color: #c9b9a6;
    font-size: 16px;
    line-height: 1.8;
    max-width: 560px;
    margin: 18px auto 0;
}

/* Form container */
div[data-testid="stForm"] {
    background: rgba(255, 248, 236, 0.045);
    border: 1px solid rgba(224, 184, 123, 0.22);
    border-radius: 18px;
    padding: 24px;
}

/* Memory and person inputs */
.stTextArea textarea,
.stTextInput input {
    background: #29221d !important;
    color: #fff3df !important;
    border: 1px solid #806347 !important;
    border-radius: 10px !important;
    caret-color: #f4d7a1 !important;
}

.stTextArea textarea:focus,
.stTextInput input:focus {
    border-color: #d8a85f !important;
    box-shadow: 0 0 0 1px rgba(216, 168, 95, 0.3) !important;
}

/* Dropdown */
.stSelectbox div[data-baseweb="select"] > div {
    background: #29221d !important;
    color: #fff3df !important;
    border: 1px solid #806347 !important;
    border-radius: 10px !important;
}

.stSelectbox div[data-baseweb="select"] span {
    color: #fff3df !important;
}

/* Dropdown menu options */
div[data-baseweb="popover"] ul {
    background: #29221d !important;
}

div[data-baseweb="popover"] li {
    color: #fff3df !important;
}

/* Buttons */
.stButton button,
.stFormSubmitButton button {
    background: #d8a85f !important;
    color: #21170f !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    min-height: 44px;
    transition: background 0.2s ease, transform 0.2s ease;
}

.stButton button:hover,
.stFormSubmitButton button:hover {
    background: #f0c982 !important;
    transform: translateY(-1px);
}

/* Generated memory card */
.memory-card {
    background: rgba(255, 248, 236, 0.05);
    border: 1px solid rgba(224, 184, 123, 0.16);
    border-left: 3px solid #d8a85f;
    padding: 24px;
    border-radius: 8px;
    line-height: 1.9;
    color: #f5ead9;
    white-space: pre-wrap;
}

/* Footer */
.footer {
    text-align: center;
    color: #b8a795;
    font-size: 12px;
    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="hero-icon">🕯️</div>
    <div class="eyebrow">A little place for what stays</div>
    <div class="hero-title">Echoes</div>
    <div class="hero-subtitle">
        Some moments deserve more than a place in our memories.
        Turn yours into words worth keeping, and give them a voice.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("### ✦ Tell us about a memory")
st.caption(
    "A small moment, a favourite person, a familiar place — "
    "start wherever feels right."
)

# ---------------- MEMORY INPUT ----------------
with st.form("memory_form"):
    memory = st.text_area(
        "Your memory",
        placeholder=(
            "I remember the rainy evenings at my grandmother's house, "
            "the smell of chai, and how she always saved the last biscuit for me..."
        ),
        height=160,
        max_chars=3000,
    )

    person = st.text_input(
        "Who or what is this memory about? (optional)",
        placeholder="e.g. Grandma, my childhood home, an old friendship",
        max_chars=100,
    )

    style = st.selectbox(
        "How would you like it to feel?",
        [
            "Warm and nostalgic",
            "Poetic and reflective",
            "Gentle and comforting",
            "Simple and heartfelt",
        ],
    )

    submitted = st.form_submit_button(
        "✦  Preserve this memory",
        use_container_width=True,
    )

# ---------------- LOCAL AI WRITING ----------------
if submitted:
    if not memory.strip():
        st.warning("Write a little about your memory first.")
    else:
        prompt = f"""
You are the writing companion behind Echoes, a gentle memory-preservation project.

Transform the user's real memory into a beautiful, personal piece of writing.

Style: {style}
Person or subject, if supplied: {person or "Not specified"}

The user's memory:
{memory}

Instructions:
- Preserve the real details and meaning the user shared.
- Write in natural, warm, emotionally thoughtful language.
- Use sensory details only when they are present in the memory or clearly framed
  as gentle imagery, not as invented facts.
- Do not invent conversations, events, promises, or biographical details.
- Do not claim to contact, hear from, or speak on behalf of someone who has died.
- Avoid clichés and excessive melodrama.
- Write around 120 to 200 words.
- Return only the finished piece, with a gentle title on the first line.
"""

        with st.spinner("Gathering your memory into words..."):
            try:
                groq_api_key = get_secret("groq_api_key") or get_secret("GROQ_API_KEY")

                if not groq_api_key:
                    st.error(
                        "Groq API key is missing. "
                        "Please add GROQ_API_KEY to your .env file."
                    )
                else:
                    client = Groq(
                        api_key=groq_api_key,
                        timeout=180.0,
                    )

                    completion = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt,
                            }
                        ],
                    )

                    result = (
                        completion.choices[0].message.content or ""
                    ).strip()

                    if not result:
                        st.error(
                            "The AI returned an empty response. "
                            "Please try again."
                        )
                    else:
                        st.session_state["echoes_memory"] = result
                        st.session_state.pop("echoes_audio", None)

            except Exception as error:
                st.error(
                    f"Something went wrong while writing: {error}"
                )


# ---------------- DISPLAY WRITING ----------------
if st.session_state.get("echoes_memory"):
    st.write("")
    st.markdown("### Your memory, gently retold")
    st.markdown(
        '<div class="memory-card">'
        + st.session_state["echoes_memory"].replace("&", "&amp;")
        .replace("<", "&lt;").replace(">", "&gt;")
        .replace("\n", "<br>")
        + "</div>",
        unsafe_allow_html=True,
    )

    st.write("")
    st.download_button(
        "↓  Keep a written copy",
        data=st.session_state["echoes_memory"],
        file_name="my_echoes_memory.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.divider()
    st.markdown("### ♫ Give your memory a voice")
    st.caption(
        "Turn your written memory into narration using ElevenLabs. "
        "This step requires your API key and an available account quota."
    )

    if st.button("♫  Create audio narration", use_container_width=True):
        api_key = get_secret("elevenlabs_api_key") or get_secret("ELEVENLABS_API_KEY")

        if not api_key:
            st.warning(
                "ElevenLabs isn't configured yet. We'll add your API key next."
            )
        else:
            try:
                with st.spinner("Giving your memory a voice..."):
                    client = ElevenLabs(api_key=api_key)
                    audio_chunks = client.text_to_speech.convert(
                        text=st.session_state["echoes_memory"][:4500],
                        voice_id="JBFqnCBsd6RMkjVDRZzb",
                        model_id="eleven_multilingual_v2",
                        output_format="mp3_44100_128",
                    )
                    st.session_state["echoes_audio"] = b"".join(audio_chunks)

            except Exception:
                st.warning(
        "♫ AI narration is taking a little pause. "
        "Please try the free browser narration below."
    )
    
    if st.session_state.get("echoes_audio"):
        st.audio(st.session_state["echoes_audio"], format="audio/mp3")
        st.download_button(
            "↓  Download your narrated memory",
            data=st.session_state["echoes_audio"],
            file_name="my_echoes_memory.mp3",
            mime="audio/mpeg",
            use_container_width=True,
        )

    
    st.markdown("#### ♫ Try free browser narration")
    st.caption(
        "Listen to your memory using your browser's built-in speech voice. "
        "Voice availability depends on your device and browser."
    )

    import json
    import streamlit.components.v1 as components

    memory_json = json.dumps(st.session_state["echoes_memory"])

    components.html(
        f"""
        <div style="font-family: sans-serif; color: #f5ead9;">
          <button id="speakBtn"
            style="padding: 10px 16px; border-radius: 8px;
                   border: 1px solid #c9a878; background: #302019;
                   color: #f5ead9; cursor: pointer;">
            ▶ Play narration (free)
          </button>
          <button id="stopBtn"
            style="padding: 10px 16px; border-radius: 8px;
                   border: 1px solid #c9a878; background: #302019;
                   color: #f5ead9; cursor: pointer; margin-left: 6px;">
            ■ Stop
          </button>
          <p id="status" style="font-size: 13px; margin-top: 10px;"></p>
        </div>

        <script>
          const memoryText = {memory_json};
          const status = document.getElementById("status");

          document.getElementById("speakBtn").onclick = () => {{
            if (!("speechSynthesis" in window)) {{
              status.textContent =
                "Speech narration is not supported by this browser.";
              return;
            }}

            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(memoryText);
            utterance.lang = "en-US";
            utterance.rate = 0.9;
            utterance.onstart = () => {{
              status.textContent = "Your memory is being narrated…";
            }};
            utterance.onend = () => {{
              status.textContent = "Narration complete.";
            }};
            utterance.onerror = () => {{
              status.textContent =
                "Narration could not start. Try another browser.";
            }};
            window.speechSynthesis.speak(utterance);
          }};

          document.getElementById("stopBtn").onclick = () => {{
            window.speechSynthesis.cancel();
            status.textContent = "Narration stopped.";
          }};
        </script>
        """,
        height=130,
    )


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    MADE WITH CARE · YOUR MEMORIES, YOUR WORDS, YOUR ECHOES
</div>
""", unsafe_allow_html=True)
