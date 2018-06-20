FROM python:slim

MAINTAINER  Andrii Bryndzak <abryndz@softserveinc.com>

ENV FLASK_PORT 5000

# Copy the application folder inside the container
COPY . /getsomeurl

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r /getsomeurl/requirements.txt

# Expose ports
EXPOSE $FLASK_PORT

# Set the default directory where CMD will execute
WORKDIR /getsomeurl

# Set the default command to execute
# when creating a new container
CMD FLASK_APP=getsomeurl.py flask run --host=0.0.0.0 -p $FLASK_PORT
