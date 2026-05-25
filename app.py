import streamlit as st
from openai import OpenAI
from pdfreader import read_pdf

# -----------------------------
# OPENROUTER API
# -----------------------------
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# -----------------------------
# READ PDF
# -----------------------------
pdf_path = "./res/moneshsys.pdf"

try:
    pages = read_pdf(pdf_path)
    pdf_text = " ".join(pages)
except:
    pdf_text = "No PDF loaded."

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="MST Chatbot",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0a66c2, #001f3f);
    font-family: Arial, sans-serif;
}

/* Floating Chatbot */
.chat-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 380px;
    max-height: 85vh;
    overflow-y: auto;
    background: rgba(30,30,30,0.95);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 0px 25px rgba(0,0,0,0.5);
}

/* Title */
.title {
    color: white;
    font-size: 26px;
    text-align: center;
    margin-bottom: 15px;
    font-weight: bold;
}

/* Chat bubbles */
.user-msg {
    background: #0a66c2;
    color: white;
    padding: 12px;
    border-radius: 15px;
    margin: 10px 0;
}

.bot-msg {
    background: white;
    color: black;
    padding: 12px;
    border-radius: 15px;
    margin: 10px 0;
}

/* Input box */
.stTextInput input {
    border-radius: 15px !important;
    padding: 10px !important;
    border: none !important;
}

/* Hide Streamlit Branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .chat-container {
        width: 90%;
        right: 5%;
        bottom: 10px;
    }
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# FLOATING CHATBOT
# -----------------------------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

st.markdown(
    '<div class="title">🤖 MST Chatbot</div>',
    unsafe_allow_html=True
)

# Show old messages
for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-msg"><b>You:</b> {msg["content"]}</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div class="bot-msg"><b>MST Chatbot:</b> {msg["content"]}</div>',
            unsafe_allow_html=True
        )

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.text_input(
    "Ask me anything about MoneshSys..."
)

# -----------------------------
# AI RESPONSE
# -----------------------------
if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    prompt = f"""
You are Monesh AI assistant.

Answer ONLY using this PDF information:

{pdf_text}

User Question:
{user_input}
"""

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

    except Exception as e:
        answer = f"Error: {str(e)}"

    # Save AI reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
