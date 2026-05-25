import streamlit as st
from openai import OpenAI
from pdfreader import read_pdf

# OpenRouter API
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# Read PDF
pdf_path = "./res/moneshsys.pdf"
pages = read_pdf(pdf_path)

# Convert PDF pages into text
pdf_text = " ".join(pages)

# Page settings
st.set_page_config(page_title="Monesh AI", layout="wide")

# Custom CSS for floating chatbot
st.markdown("""
<style>

.chat-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 350px;
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
}

.title {
    color: white;
    font-size: 22px;
    text-align: center;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# Floating Chatbot
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

st.markdown(
    '<div class="title">Monesh AI Chatbot</div>',
    unsafe_allow_html=True
)

# User Input
user_input = st.text_input("Ask me anything")

# AI Response from PDF
if user_input:

    prompt = f"""
    Answer only using this PDF information:

    {pdf_text}

    User Question:
    {user_input}
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    st.write(answer)

st.markdown("</div>", unsafe_allow_html=True)
