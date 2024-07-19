from datetime import datetime, timedelta, timezone, time
import urllib.request
from dotenv import load_dotenv
import os
import json

# loading the API key
load_dotenv()
API_KEY = os.getenv('API_KEY')

# get icons data
def get_icons(period) :
    with open(f'data/icons_{period}.json') as json_file :
        icons = json.load(json_file)
    return icons


# compute the current datetime given the offest
def get_current_datetime(offset_hours, offset_minutes) :
    try:
        offset = timezone(timedelta(hours = offset_hours, minutes = offset_minutes))
        current_datetime = datetime.now(offset)
        return current_datetime
    except Exception as e:
        return str(e)


# returns the coordinates of a given city
def get_coordinates(city, state = '', country = '', API = API_KEY) :
    response = urllib.request.urlopen(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={API}'
    ).read()

    data = (json.loads(response))[0]
    latitude, longtitude = data['lat'], data['lon']
    return latitude, longtitude


# get current weather given the coordinates
def get_weather(lat, lon, API = API_KEY) :
    response = urllib.request.urlopen(
        f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}'
    ).read()

    data = json.loads(response)

    hours = data['timezone'] / 3600
    minutes = (data['timezone'] % 3600) / 60
    current_time = get_current_datetime(hours, minutes)

    icon_description = data['weather'][0]['description']
    description = icon_description

    if 'thunderstorm' in icon_description :
        description = 'thunderstorm'
    elif 'drizzle' in icon_description :
        description = 'drizzle'
    elif 'shower rain' in icon_description :
        description = 'shower rain'
    elif 'rain' in icon_description :
        description = 'rain'
    elif 'snow' in icon_description or 'sleet' in icon_description:
        description = 'snow'

    if current_time.time() > time(18, 0) or current_time.time() < time(4, 0) :
        icon_description = get_icons('night')[description]
    else :
        icon_description = get_icons('day')[description]

    link = f'/static/images/{icon_description}.svg'
    description = icon_description = data['weather'][0]['main']
    country = data['sys']['country']
    if country == 'IL' :
        country = 'PS'
    speed = "{:.2f}".format(data['wind']['speed'] * 3.6)

    returned_data = {
        'country' : country,
        'city_name' : data['name'],
        'current_time' : str(current_time.strftime("%Y-%m-%d, %H:%M")),
        'temperature' : str(int(data['main']['temp']) - 273),
        'feels_like' : str(int(data['main']['feels_like'] - 273)),
        'temp_discription' : data['weather'][0]['main'],
        'wind' : str(speed),
        'pressure' : str(data['main']['pressure']),
        'humidity' : str(data['main']['humidity']),
        'description' : description,
        'icon' : link
    }

    return returned_data