import requests

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.settings import ModelSettings

from config import *

# Weather output model
class WeatherForecast(BaseModel):
    location: str
    description: str
    temperature_celsius: float


# Create Agent
weather_agent = Agent(
    model="groq:llama-3.1-8b-instant",
    model_settings=ModelSettings(
        temperature=0.2
    ),
    output_type=str,
    system_prompt="""
You are a helpful weather assistant.

Always use the get_weather_forecast tool whenever a user asks about weather.

After receiving the tool result, answer naturally.
"""
)


# Register Tool
@weather_agent.tool
def get_weather_forecast(
    ctx: RunContext,
    city: str
) -> WeatherForecast:

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(
        BASE_URL,
        params=params
    )

    result = response.json()

    if response.status_code != 200:
        raise Exception(result)

    return WeatherForecast(
        location=result["name"],
        description=result["weather"][0]["description"].capitalize(),
        temperature_celsius=result["main"]["temp"]
    )


# Function Streamlit will call
def ask_weather(question: str):

    result = weather_agent.run_sync(question)

    return result.output