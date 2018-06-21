FROM python:slim

MAINTAINER  Andrii Bryndzak <abryndz@softserveinc.com>

# Copy the application folder inside the container
COPY . /grpc_weather_api

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r /grpc_weather_api/requirements.txt

# Expose ports
EXPOSE 5000

# Required environment variables
# WEATHER_API_URL

# Set the default directory where CMD will execute
WORKDIR /grpc_weather_api

# Set the default command to execute
# when creating a new container
CMD FLASK_APP=src/grpc_weather_api.py flask run --host=0.0.0.0 -p 5000
