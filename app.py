from flask import Flask, request, render_template, redirect, jsonify
from weather import get_coordinates, get_weather
import os
import json


app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def index() :
    cities = ['London', 'Tokyo', 'Sydney', 'Algiers', 'NYC']
    sources = []

    for town in cities :
        lan, lon = get_coordinates(city = town)
        sources.append(get_weather(lan, lon))

    state, country  = '', ''

    if request.method == 'POST' :
        input = request.form['search_input']
        result = input.split(',')
        city = result[0]

        if len(result) == 3 :
            state, country = result[1], result[2]
        elif len(result) == 2 :
            country = result[1]
    else :
        city = 'Algiers'

    city = city.replace(' ', '-')
    country = country.replace(' ', '')
    state = state.replace(' ', '')
    
    try :
        lant, long = get_coordinates(city, state, country)
        data = get_weather(lant, long)
    except :
        return redirect('/')
    
    return render_template('index.html', html_data = data, sources = sources)

@app.route('/get_cities')
def get_cities() :
    json_path = os.path.join(app.root_path, 'data', 'cities.json')

    with open(json_path) as json_file:
        data = json.load(json_file)
    return jsonify(data)
        

if __name__ == "__main__" :
    app.run(debug = True)