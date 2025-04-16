# Weather App (Tkinter + OpenWeatherMap)

A simple desktop weather application built using Python, Tkinter, and the OpenWeatherMap API.
It shows the current weather, temperature, humidity, and pressure for any city or country you enter.

##🔧 Features
Get weather details for any city

Shows:

🌡️ Temperature (Celsius & Fahrenheit)

🌧️ Weather condition (Clear, Rain, etc.)

💧 Humidity

🌬️ Pressure

Built with Tkinter GUI

Uses the OpenWeatherMap API

##🚀 How to Run
1. Clone the repo :
   ```
   git clone https://github.com/mustakintopu/py_project.git
   cd py_project
   ```

3. Install required packages
Make sure you have Python installed. Then run:
```
pip install pillow requests
```

5. Get an OpenWeatherMap API Key
Go to https://openweathermap.org/api
Sign up and get your API key

Replace the API key in the script:
self.api_key = 'YOUR_API_KEY'

4. Run the app:
   ```
   python weather/main.py
   ```


##⚠️ Notes
Make sure all image files (icon.png, etc.) are in the same folder as the Python script.
The temperature from the API is in Kelvin by default — it is converted to Celsius & Fahrenheit in the code.

##📜 License
This project is open-source. Feel free to use, modify, or contribute!
