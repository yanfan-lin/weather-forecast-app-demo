import os
import requests
from dotenv import load_dotenv

# Load API key as environment variable from .env
load_dotenv()

# Get an API key from https://openweathermap.org/
API_KEY = os.getenv("API_KEY")

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&APPID={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]

    # Each day contains 8 data points (3-hour intervals)
    num_of_values = 8 * forecast_days

    filtered_data = filtered_data[:num_of_values]

    return filtered_data

if __name__ == "__main__":
    get_data("Vancouver", 5)