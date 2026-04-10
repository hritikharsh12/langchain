import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="CHAT BOT", page_icon="🤖", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Sora:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Sora', sans-serif;
    background-color: #0d0f14;
    color: #e8e8f0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 0; max-width: 780px; }

.chat-title {
    font-family: 'Space Mono', monospace;
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #7b8cff;
    margin-bottom: 0.2rem;
}
.chat-subtitle {
    font-size: 0.78rem;
    color: #555a7a;
    letter-spacing: 0.06em;
    margin-bottom: 1.6rem;
}
.chat-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding-bottom: 1rem;
}
.bubble {
    max-width: 78%;
    padding: 0.75rem 1.1rem;
    border-radius: 18px;
    line-height: 1.65;
    font-size: 0.93rem;
    word-break: break-word;
    animation: fadeUp 0.25s ease both;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}
.bubble-user {
    background: linear-gradient(135deg, #3d4aff 0%, #6c5ce7 100%);
    color: #fff;
    align-self: flex-end;
    border-bottom-right-radius: 4px;
}
.bubble-bot {
    background: #1a1d2e;
    border: 1px solid #252840;
    color: #d4d6f0;
    align-self: flex-start;
    border-bottom-left-radius: 4px;
}
.bubble-row { display: flex; flex-direction: column; }
.role-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 4px;
    padding-left: 4px;
}
.role-label-user { color: #7b8cff; text-align: right; }
.role-label-bot  { color: #55607a; }

.stTextInput > div > div > input {
    background: #13162a !important;
    border: 1px solid #252840 !important;
    border-radius: 12px !important;
    color: #e8e8f0 !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 0.92rem !important;
    padding: 0.65rem 1rem !important;
    caret-color: #7b8cff;
}
.stTextInput > div > div > input:focus {
    border-color: #3d4aff !important;
    box-shadow: 0 0 0 3px rgba(61,74,255,0.15) !important;
}
.stTextInput > div > div > input::placeholder { color: #3a3f5c !important; }

.stButton > button {
    background: linear-gradient(135deg, #3d4aff 0%, #6c5ce7 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.1em !important;
    padding: 0.65rem 1rem !important;
    cursor: pointer !important;
    transition: opacity 0.15s ease !important;
    height: 46px !important;
    white-space: nowrap !important;
    min-width: 70px !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

.divider {
    border: none;
    border-top: 1px solid #1e2138;
    margin: 1rem 0 0.6rem;
}
.stSpinner > div { border-top-color: #7b8cff !important; }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-7B-Instruct",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
        temperature=0.7,
    )
    return ChatHuggingFace(llm=llm)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]
if "display_messages" not in st.session_state:
    st.session_state.display_messages = []
if "input_key" not in st.session_state:
    st.session_state.input_key = 0   # bumping remounts widget → clears the box
if "pending_input" not in st.session_state:
    st.session_state.pending_input = ""


def on_enter():
    """Fires when user presses Enter in the text box."""
    val = st.session_state[f"msg_{st.session_state.input_key}"]
    if val.strip():
        st.session_state.pending_input = val
        st.session_state.input_key += 1   # clears box on next render


st.markdown('<div class="chat-title">⬡ Qwen Chat</div>', unsafe_allow_html=True)
st.markdown('<div class="chat-subtitle">Qwen2.5-7B-Instruct · LangChain · HuggingFace</div>', unsafe_allow_html=True)

chat_html = '<div class="chat-wrapper">'
for msg in st.session_state.display_messages:
    if msg["role"] == "user":
        chat_html += f"""
        <div class="bubble-row">
            <div class="role-label role-label-user">You</div>
            <div class="bubble bubble-user">{msg["text"]}</div>
        </div>"""
    else:
        chat_html += f"""
        <div class="bubble-row">
            <div class="role-label role-label-bot">Qwen</div>
            <div class="bubble bubble-bot">{msg["text"]}</div>
        </div>"""
chat_html += '</div>'
st.markdown(chat_html, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([6, 1, 1])

with col1:
    current_key = f"msg_{st.session_state.input_key}"
    st.text_input(
        label="message",
        label_visibility="collapsed",
        placeholder="Type a message and press Enter…",
        key=current_key,
        on_change=on_enter,   # Enter key submits
    )

with col2:
    send_clicked = st.button("Send", use_container_width=True)

with col3:
    clear_clicked = st.button("Clear", use_container_width=True)

if send_clicked:
    val = st.session_state.get(current_key, "")
    if val.strip():
        st.session_state.pending_input = val
        st.session_state.input_key += 1

if clear_clicked:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]
    st.session_state.display_messages = []
    st.session_state.pending_input = ""
    st.session_state.input_key += 1
    st.rerun()

if st.session_state.pending_input.strip():
    user_text = st.session_state.pending_input.strip()
    st.session_state.pending_input = ""

    model = load_model()
    st.session_state.chat_history.append(HumanMessage(content=user_text))
    st.session_state.display_messages.append({"role": "user", "text": user_text})

    with st.spinner("Thinking…"):
        result = model.invoke(st.session_state.chat_history)

    bot_reply = result.content
    st.session_state.chat_history.append(AIMessage(content=bot_reply))
    st.session_state.display_messages.append({"role": "bot", "text": bot_reply})

    st.rerun()
    

