"""
Weather Data Fetching and Visualization Script

This script:
1. Fetches real-time weather data from OpenWeatherMap API
2. Extracts important parameters
3. Visualizes the data using Matplotlib and Seaborn
"""

import requests
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
#  API CONFIGURATION
# -------------------------------
API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
CITY = "Hyderabad"

# -------------------------------
#  FETCH DATA FROM API
# -------------------------------
def fetch_weather_data(city):
    """
    Fetch weather data from OpenWeatherMap API
    
    Args:
        city (str): Name of the city
    
    Returns:
        dict: JSON response from API
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

# -------------------------------
#  PROCESS DATA
# -------------------------------
def process_weather_data(data):
    """
    Extract important weather parameters
    
    Args:
        data (dict): API response
    
    Returns:
        dict: Processed weather data
    """
    weather_info = {
        "Temperature (°C)": data['main']['temp'],
        "Humidity (%)": data['main']['humidity'],
        "Pressure (hPa)": data['main']['pressure']
    }
    return weather_info

# -------------------------------
#  VISUALIZATION
# -------------------------------
def visualize_data(weather_info):
    """
    Create bar chart visualization
    
    Args:
        weather_info (dict): Processed weather data
    """
    labels = list(weather_info.keys())
    values = list(weather_info.values())

    # Matplotlib Bar Chart
    plt.figure()
    plt.bar(labels, values)
    plt.title("Weather Data Visualization")
    plt.xlabel("Parameters")
    plt.ylabel("Values")
    plt.show()

    # Seaborn Bar Chart
    plt.figure()
    sns.barplot(x=labels, y=values)
    plt.title("Weather Data (Seaborn)")
    plt.show()

# -------------------------------
#  MAIN FUNCTION
# -------------------------------
def main():
    """
    Main execution function
    """
    data = fetch_weather_data(CITY)
    
    if data:
        weather_info = process_weather_data(data)
        print("Weather Data:", weather_info)
        visualize_data(weather_info)

# Run the script
if __name__ == "__main__":
    main()
