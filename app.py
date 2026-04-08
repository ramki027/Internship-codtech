"""
Streamlit Weather Dashboard

This app:
- Takes user input (city)
- Fetches live weather data
- Displays results interactively
"""

import streamlit as st
import requests

# -------------------------------
#  API CONFIGURATION
# -------------------------------
API_KEY = "your_api_key_here"

# -------------------------------
#  STREAMLIT UI
# -------------------------------
st.title("🌦️ Weather Dashboard")

city = st.text_input("Enter City Name", "Hyderabad")

# -------------------------------
#  FETCH DATA
# -------------------------------
if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract data
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather = data['weather'][0]['description']

        # Display data
        st.subheader(f"Weather in {city}")
        st.write(f"🌡 Temperature: {temperature} °C")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"ضغط Pressure: {pressure} hPa")
        st.write(f"☁ Condition: {weather}")

    else:
        st.error("City not found or API error")
