# 🌤️ AI Weather Assistant

An AI-powered Weather Assistant built using **Pydantic AI**, **Groq**, **Streamlit**, and the **OpenWeather API**.

The application demonstrates how to build an AI agent with custom tools. Instead of relying only on an LLM's knowledge, the agent decides when to call a weather tool to retrieve real-time weather information before generating a natural language response.

---

## Features

- AI Agent built with Pydantic AI
- Groq (Llama 3.1) as the reasoning model
- Custom Weather Tool
- Live weather using OpenWeather API
- Streamlit chat interface
- Structured output using Pydantic BaseModel
- Environment variable support
- Ready for Streamlit Cloud deployment

---

## Architecture

```text
User
   │
   ▼
Streamlit UI
   │
   ▼
Pydantic AI Agent
   │
   ▼
Groq LLM
   │
Decides whether a tool is needed
   │
   ▼
Weather Tool
   │
   ▼
OpenWeather API
   │
   ▼
Weather Response
   │
   ▼
Groq generates final answer
```

---

## Tech Stack

- Python
- Streamlit
- Pydantic AI
- Groq
- OpenWeather API
- Requests
- Python Dotenv

---

## Project Structure

```text
weather-ai-agent/
│
├── app.py
├── weather_agent.py
├── config.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/weather-ai-agent.git

cd weather-ai-agent
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## How It Works

1. The user asks a weather-related question.
2. The Pydantic AI Agent sends the request to Groq.
3. Groq determines that live weather data is required.
4. The agent invokes the custom `get_weather_forecast()` tool.
5. The tool calls the OpenWeather API.
6. The weather data is returned to Groq.
7. Groq generates a natural language response.
8. Streamlit displays the response to the user.

---

## What You'll Learn

- Creating AI agents with Pydantic AI
- Registering custom tools
- Integrating Groq as an LLM
- Calling external REST APIs
- Building AI applications with Streamlit
- Working with structured outputs using Pydantic

---

## Future Improvements

- 5-day weather forecast
- Weather icons and animations
- Voice input
- Chat history persistence
- Multi-tool AI assistant
- Maps and weather visualizations
- Streaming responses

---

## License

This project is licensed under the MIT License.
