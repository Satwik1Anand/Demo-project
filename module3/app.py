import os
from dotenv import load_dotenv
import streamlit as st
from anthropic import Anthropic

# Load environment variables
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = "claude-v1"

if not API_KEY:
    raise ValueError("API key not found. Please set ANTHROPIC_API_KEY in .env file.")

client = Anthropic(api_key=API_KEY)

st.title("Streaming Chat with Claude API")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

def stream_response(messages):
    response_text = ""
    # Stream response from Claude API
    for chunk in client.messages.stream(
        model=MODEL,
        messages=messages,
        stream=True,
        max_tokens=100,
    ):
        response_text += chunk["completion"]
        yield response_text

# Input area
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to session state and display
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Prepare messages for API
    api_messages = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in st.session_state.messages
    ]

    # Placeholder for assistant message
    assistant_message = st.chat_message("assistant")
    message_placeholder = assistant_message.empty()

    # Stream and update UI
    full_response = ""
    for partial_response in stream_response(api_messages):
        full_response = partial_response
        message_placeholder.markdown(full_response)

    # Save full assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_response})