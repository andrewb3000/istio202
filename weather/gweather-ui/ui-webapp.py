from flask import Flask
from flask import abort
import requests
import os

WEATHER_API_URL=os.environ['WEATHER_API_URL']
# WEATHER_API_URL='http://192.168.56.58:8000/weather'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/weather")
def weather():
    try:
        weather_info = requests.get(WEATHER_API_URL)
        if weather_info.status_code == 200:
            return weather_info.content
        else:
            abort(weather_info.status_code)
    except Exception as e:
        abort(502)
