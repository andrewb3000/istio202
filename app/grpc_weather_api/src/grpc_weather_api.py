from flask import Flask
from flask import abort
from flask import jsonify
import grpc
import weather_pb2 as weather_messages
import weather_pb2_grpc as weather_service
import os
import json

WEATHER_SERVICE_URL=os.environ['WEATHER_SERVICE_URL']
WEATHER_LOCATION=os.environ['WEATHER_LOCATION']

def grpcWeatherRequest(location):
    channel = grpc.insecure_channel(WEATHER_SERVICE_URL)
    try:
        grpc.channel_ready_future(channel).result(timeout=5)
    except grpc.FutureTimeoutError:
        raise ConnectionException('Error connecting to gweather server')
    else:
        stub = weather_service.WeatherStub(channel)
    response_list = []
    try:
        locations = json.loads(location)
        print(locations)
    except ValueError:
        locations = []
        locations.append(location)
    for loc in locations:
        glocation = weather_messages.WeatherRequest(location=loc)
        response = stub.CurrentConditions(glocation)
        print(response)
        if response.found and response.description != "":
            response_json = {'Location': loc, 'Temperature': response.temperature, 'Description': response.description}
        else:
            response_json = {'Location': loc, 'Description': 'Could not found weather information'}
        response_list.append(response_json)
    # print(response_json)
    return response_list


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "gWeather API"

@app.route("/getweather", methods=['GET'])
def weather():
    try:
        weather_info = str(grpcWeatherRequest(WEATHER_LOCATION)).replace('\n', ' ')
        weather_info = grpcWeatherRequest(WEATHER_LOCATION)
        return jsonify(weather_info)
    except:
        abort(502)
