from flask import Flask
from flask import abort
from flask import jsonify
import grpc
import weather_pb2 as weather_messages
import weather_pb2_grpc as weather_service
import os

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
    # print(type(location))
    # if type(location) is list:
    #     response = []
    #     for location_name in location:
    #         glocation = weather_messages.WeatherRequest(location=location_name)
    #         response_temp = stub.CurrentConditions(glocation)
    #         if response_temp:
    #             # print(response_temp)
    #             response.append('Location: ' + location_name + ' ' + str(response_temp).replace('\n', ' '))
    #         else:
    #             raise FetchException('Could not get weather info')
    # else:
    glocation = weather_messages.WeatherRequest(location=location)
    response = stub.CurrentConditions(glocation)
    print(response)
    if response.found and response.description != "":
        response_json = {'Location': location, 'Temperature': response.temperature, 'Description': response.description}
    else:
        response_json = {'Location': location, 'Description': 'Could not found weather information'}
    # print(response_json)
    return response_json


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "gWeather API"

@app.route("/getweather", methods=['GET'])
def weather():
    try:
        # weather_info = str(grpcWeatherRequest(WEATHER_LOCATION)).replace('\n', ' ')
        weather_info = grpcWeatherRequest(WEATHER_LOCATION)
        return jsonify(weather_info)
    except:
        abort(502)
