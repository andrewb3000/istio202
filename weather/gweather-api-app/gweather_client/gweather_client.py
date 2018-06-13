import grpc
import sys
import time

import weather_pb2 as weather_messages
import weather_pb2_grpc as weather_service

SERVER_URL='localhost:9000'
LOCATIONS=['Kiev', 'Berlin']

def getWeather():
	channel = grpc.insecure_channel(SERVER_URL)
	try:
		grpc.channel_ready_future(channel).result(timeout=5)
	except grpc.FutureTimeoutError:
		raise Exception('Error connecting to gweather server')
		# sys.exit('Error connecting to server')
	else:
		stub = weather_service.WeatherStub(channel)
	response = []
	for loc_name in LOCATIONS:
		location = weather_messages.WeatherRequest(location=loc_name)
		response_temp = stub.CurrentConditions(location)
		if response_temp:
			print(response_temp)
			response.append('Location: ' + loc_name + ' ' + str(response_temp).replace('\n', ' '))
			# time.sleep(5)
	return response

def main():
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

if __name__ == '__main__':
    main()