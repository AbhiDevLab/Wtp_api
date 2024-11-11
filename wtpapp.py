import requests
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_weather_and_pollution(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def interpret_aqi(pm2_5):
    if pm2_5 <= 12:
        return "Good", "green"
    elif pm2_5 <= 35.4:
        return "Moderate", "yellow"
    elif pm2_5 <= 55.4:
        return "Unhealthy for Sensitive Groups", "orange"
    elif pm2_5 <= 150.4:
        return "Unhealthy", "red"
    elif pm2_5 <= 250.4:
        return "Very Unhealthy", "purple"
    else:
        return "Hazardous", "maroon"

def show_weather_and_pollution():
    city = city_entry.get()
    data = get_weather_and_pollution(city)
    if data:
        weather = data['current']
        condition = weather['condition']['text']
        temp_c = weather['temp_c']
        humidity = weather['humidity']
        wind_kph = weather['wind_kph']
        
        air_quality = weather['air_quality']
        pm2_5 = air_quality['pm2_5']
        pm10 = air_quality['pm10']
        co = air_quality['co']
        no2 = air_quality['no2']
        o3 = air_quality['o3']
        
        aqi_description, color = interpret_aqi(pm2_5)

        result.set(
            f"{city.capitalize()} Weather:\n"
            f"Condition: {condition}\n"
            f"Temperature: {temp_c}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_kph} km/h\n\n"
            f"Pollution Levels:\n"
            f"PM2.5: {pm2_5} μg/m³\n"
            f"PM10: {pm10} μg/m³\n"
            f"CO: {co} μg/m³\n"
            f"NO2: {no2} μg/m³\n"
            f"O3: {o3} μg/m³\n\n"
            f"AQI: {aqi_description}"
        )
        aqi_label.config(text=f"AQI Level: {aqi_description}", bg=color)
    else:
        messagebox.showerror("Error", "Unable to retrieve data. Please check the city name or try again later.")

window = tk.Tk()
window.title("Weather & Pollution App")

city_entry = tk.Entry(window)
city_entry.pack()

fetch_button = tk.Button(window, text="Get Weather & Pollution Data", command=show_weather_and_pollution)
fetch_button.pack()

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, wraplength=400, justify="left")
result_label.pack()

aqi_label = tk.Label(window, text="AQI Level:", font=("Arial", 12, "bold"), bg="white")
aqi_label.pack(pady=5, fill="x")

window.mainloop()
