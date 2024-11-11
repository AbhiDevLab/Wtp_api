**Weather & Pollution Monitoring App**

This Weather & Pollution Monitoring App is a Python-based desktop application that provides real-time weather and air quality data for any specified city. Built with the Tkinter library, it offers a simple user interface where users can enter a city name and receive up-to-date information on weather conditions, temperature, humidity, wind speed, and pollution levels (including PM2.5, PM10, CO, NO2, and O3). The app also interprets the Air Quality Index (AQI) and displays the air quality level with a color-coded indication.

1) Features

- **Real-Time Weather Data**: Displays current temperature, weather conditions, humidity, and wind speed.
- **Air Quality Monitoring**: Provides key pollution indicators such as PM2.5, PM10, CO, NO2, and O3.
- **AQI Interpretation**: Interprets and color-codes the AQI based on PM2.5 levels for easy understanding of air quality.
- **Simple Interface**: Built with Tkinter for a straightforward, user-friendly experience.

2) Technologies Used

- **Python**: Core language used for development.
- **Tkinter**: For creating a simple and interactive GUI.
- **Weather API**: Fetches real-time weather and air quality data (ensure `.env` file includes your API key).
- **dotenv**: Used to securely load the API key from an environment file.

3) Setup

1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Create a `.env` file and add your API key as `API_KEY=your_api_key_here`.
4. Run the app with `python app.py`.
