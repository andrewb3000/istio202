FROM python:slim

MAINTAINER  Andrii Bryndzak <abryndz@softserveinc.com>

# Copy the application folder inside the container
COPY . /gweather

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r /gweather/requirements.txt

# Expose ports
EXPOSE 8000

# Set the default directory where CMD will execute
WORKDIR /gweather

# Set the default command to execute
# when creating a new container
CMD gunicorn -b :8000 --pythonpath /gweather/gweather_client api-webapp
