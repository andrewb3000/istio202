from flask import Flask
from flask import abort
from flask import jsonify
from flask import request
import grpc
import weather_pb2 as weather_messages
import weather_pb2_grpc as weather_service
import os
import json

WEATHER_SERVICE_URL=os.environ['WEATHER_SERVICE_URL']
WEATHER_LOCATION=os.environ['WEATHER_LOCATION']

def getForwardHeaders(request):
    headers = {}
    user_cookie = request.cookies.get("user")
    if user_cookie:
        headers['Cookie'] = 'user=' + user_cookie
    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]
    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            #print "incoming: "+ihdr+":"+val
    return headers

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
        # print(locations)
    except ValueError:
        locations = []
        locations.append(location)
    for loc in locations:
        print(loc)
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
    headers = getForwardHeaders(request)
    metadata = list(headers.items())
    try:
        weather_info = grpcWeatherRequest(WEATHER_LOCATION, metadata=metadata)
        return jsonify(weather_info)
    except:
        abort(502)
