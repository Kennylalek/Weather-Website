# Flask Weather Website

This is a simple Flask application that provides weather forecasts using the OpenWeatherMap API. The website allows users to search for the weather in different locations and displays the weather data.

## Features

- Search for weather information by city name
- Displays current weather, temperature, humidity, wind speed and pressure.
- Uses a third-party weather API to fetch weather data.
- Simple and clean user interface.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Kennylalek/Weather-Website.git
    cd Weather-Website
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - This application uses [OpenWeatherMap API](https://openweathermap.org/) to fetch weather data. Sign up for an API key.
    - Create a `.env` file in the root directory of your project.
    - Add your OpenWeatherMap API key to the `.env` file:
    
        ```
        API_KEY = your_openweathermap_api_key
        ```

## Usage

1. **Run the application:**
    ```sh
    flask run
    ```

2. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000
    ```

3. **Enter a city name in the search bar to get the weather information.**

## Project Structure
```plaintext
.
├── app.py                  # Main application file
├── weather.py              # Contains utility functions
├── templates
│   └── index.html          # HTML template for the website
├── static
│   ├── css
│   │   └── style.css       # CSS styles
│   ├── js
│   │   └── script.js       # JavaScript file
│   └── images              # Directory for weather icons from GitHub
├── data                    # Contains files to link each weather condition with an icon
│   ├── icons_day.json      
|   ├── icons_night.json 
|   └── cities.json         # List of all cities    
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Dependencies

- Flask
- Requests
- Python-dotenv

Make sure to install all dependencies listed in the `requirements.txt` file.

## Credits

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Weather icons from [Makin-Things](https://github.com/Makin-Things/weather-icons.git)
