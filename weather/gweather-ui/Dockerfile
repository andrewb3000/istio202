FROM python:slim

MAINTAINER  Andrii Bryndzak <abryndz@softserveinc.com>

# Copy the application folder inside the container
COPY . /gweather_ui

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r /gweather_ui/requirements.txt

# Expose ports
EXPOSE 5000

# Set the default directory where CMD will execute
WORKDIR /gweather_ui

# Set the default command to execute
# when creating a new container
CMD FLASK_APP=ui-webapp.py flask run --host=0.0.0.0
