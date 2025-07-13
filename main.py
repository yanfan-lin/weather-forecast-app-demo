import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")

location = st.text_input("Enter a City Name: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the Number of Forecasted Days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} day(s) in {location}")

if location:

    # Display an error message if an invalid city name is entered
    try:
        filtered_data = get_data(location, days)


        if option == "Temperature":
            # Extract and convert temperature data to be integers in Celsius
            temperature = [int(dict["main"]["temp"] / 10) for dict in filtered_data]

            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(x=dates, y=temperature, labels={"x": "Date",
                                                             "y": "Temperature(°C)"}
                             , markers=True
                             )
            st.plotly_chart(figure)

        if option == "Sky":
            # Mapping weather conditions to corresponding images
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                     "Rain": "images/rain.png", "Snow": "images/snow.png"}

            # Extract sky conditions
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

            image_path = [images[condition] for condition in sky_conditions]

            st.image(image_path, width=115)

    except KeyError:
        st.error("Invalid city name. Please try again.")






