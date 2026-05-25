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

# Convert pages into one big text
pdf_text = " ".join(pages)

# Website Title
st.title("Monesh AI Chatbot")

# User Input
user_input = st.text_input("Ask me anything")

if user_input:

    # Send PDF content + question to AI
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

    st.write("AI:", answer)