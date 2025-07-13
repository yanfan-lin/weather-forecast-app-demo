# 🌦️ Weather Forecast App

A simple web app built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/python/) to display weather forecasts for any city using the OpenWeatherMap API.

---

##  Features

-  Search for any city
-  Select forecast days (1–5)
-  View temperature trends 
-  View sky conditions
-  Uses real-time data from OpenWeatherMap API

---


##  📁 Project Structure

weather-forecast-app/
- ├── images/
- │   ├── clear.png
- │   ├── cloud.png
- │   ├── rain.png
- │   └── snow.png
- ├── app.py
- ├── backend.py
- ├── requirements.txt
- ├── .env              
- └── README.md

---

## 📦 Requirements

This project uses Python and the following packages (see `requirements.txt`):

- `streamlit`
- `plotly`
- `requests`
- `pandas`
- `python-dotenv`

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

##  Setup API Key

Get your free API key from https://openweathermap.org/

Create a .env file in the root of your project:

```commandline
API_KEY = your_api_key_here
```

### ⚠️ Make sure to include .env in .gitignore file

---

##  How to Run

In your terminal, from the project root directory:

```commandline
streamlit run app.py
```

---
