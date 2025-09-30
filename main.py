import streamlit as st
import requests
import json

# Server URL
URL = "http://localhost:11434/api/generate"
HEADERS = {"Content-Type": "application/json"}

# Maintain chat history
if "history" not in st.session_state:
    st.session_state.history = []

st.title("Local CodeLlama Chatbot")

# User input
user_input = st.text_area("Enter your prompt:", height=100)

if st.button("Send"):
    if user_input.strip() != "":
        # Append user prompt to history
        st.session_state.history.append(user_input)
        final_prompt = "\n".join(st.session_state.history)

        # Prepare request
        data = {
            "model": "codellama:latest",
            "prompt": final_prompt,
            "stream": False
        }

        # Send request to Ollama server
        response = requests.post(URL, headers=HEADERS, data=json.dumps(data))

        if response.status_code == 200:
            response_json = response.json()
            bot_response = response_json["response"]

            # Show bot response
            st.text_area("Response:", value=bot_response, height=200)

            # Append bot response to history
            st.session_state.history.append(bot_response)
        else:
            st.error(f"Error: {response.text}")
