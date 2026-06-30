import streamlit as st

from weather_agent import ask_weather

st.set_page_config(
    page_title="Weather AI",
    page_icon="🌤️"
)

st.title("🌤️ AI Weather Assistant")

st.write(
    "AI agent using Pydantic AI with Groq as the reasoning model, and added a custom weather tool that fetches live weather data from the OpenWeather API. When a user asks about the weather, the agent decides to use the tool, retrieves the live data, and then uses Groq to generate a natural language response."
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input(
    "Ask about the weather..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):

        answer = ask_weather(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)