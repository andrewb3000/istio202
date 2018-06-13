FROM python:slim

MAINTAINER  Andrii Bryndzak <abryndz@softserveinc.com>

# Add the application resources URL
# RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(cat /etc/os-release | grep VERSION_CODENAME | cut -d'=' -f2) main universe" >> /etc/apt/sources.list

# Update the sources list
# RUN apt update

# Install basic applications
# RUN ...

# Install Python and Basic Python Tools
# RUN apt install -y python-pip

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
