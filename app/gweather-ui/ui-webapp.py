from flask import Flask
from flask import abort
import requests
import os
import time

WEATHER_API_URL=os.environ['WEATHER_API_URL']
# WEATHER_API_URL='http://192.168.56.58:8000/weather'

app = Flask(__name__)

@app.route("/")
def hello():
    return "gWeather UI"

@app.route("/weather")
def weather():
    try:
        weather_info = requests.get(WEATHER_API_URL)
        if weather_info.status_code == 200:
            print(type(weather_info.content))
            output = time.ctime() + ' <br> \n' + weather_info.content.decode('utf-8')
            # return weather_info.content
            return output
        else:
            abort(weather_info.status_code)
    except Exception as e:
        abort(502)
