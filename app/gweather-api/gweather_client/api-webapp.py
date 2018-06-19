import falcon
import json
import gweather_client as gweather
import re
import logging
import sys
import os


LOGLEVEL=logging.INFO

## Logging to file
# file_path = sys.modules[__name__].__file__
# project_path = os.path.dirname(os.path.dirname(file_path))
# log_location = project_path + '/logs/'
# if not os.path.exists(log_location):
#     os.makedirs(log_location)
# file_name = 'gweather.log'
# file_location = log_location + file_name
# logging.basicConfig(format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s', filename=file_location, level=LOGLEVEL)

## Logging to stdout
logging.basicConfig(format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s', level=LOGLEVEL)
logger = logging.getLogger(__name__)


class RootResource(object):
    def on_get(self, req, resp):
        doc = {u'message': u'gRPC-Weather API'}
        resp.media = doc
        resp.status = falcon.HTTP_200


class WeatherResource(object):
    def on_get(self, req, resp):
        try:
            doc = gweather.getWeather()
            resp.media = doc
            resp.status = falcon.HTTP_200
        except Exception as e:
            logger.error('500 Internal Server Error: ' + str(e))
            raise falcon.HTTPInternalServerError(description=str(e))


api = application = falcon.API()

api.add_route('/', RootResource())
api.add_route('/weather', WeatherResource())
# api.add_route('/test', TestResource())
