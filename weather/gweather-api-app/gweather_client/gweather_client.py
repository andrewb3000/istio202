# import grpc
import sys
import time

import weather_pb2 as weather_messages
import weather_pb2_grpc as weather_service

SERVER_URL='localhost:9000'
LOCATIONS=['Kiev', 'Berlin', 'London', 'Lviv']

channel = grpc.insecure_channel(SERVER_URL)
try:
	grpc.channel_ready_future(channel).result(timeout=5)
except grpc.FutureTimeoutError:
	sys.exit('Error connecting to server')
else:
	stub = weather_service.WeatherStub(channel)

for loc_name in LOCATIONS:
	location = weather_messages.WeatherRequest(location=loc_name)
	response = stub.CurrentConditions(location)
	if response:
		print('Location: ' + loc_name)
		print(response)
	# time.sleep(5)
