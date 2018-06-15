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

#     def on_post(self, req, resp):
#         try:
#             if req.content_length:
#                 # Only proceed if request is not empty
#                 request = json.load(req.stream)
#                 logger.debug('Request: ' + str(request))
#             else:
#                 raise falcon.HTTPBadRequest(description='Empty request body not allowed')
#             # Get checks from Pingdom using pingdom.py
#             pd_checks = pingdom.get_checks()
#             response = []
#             for target in request['targets']:
#                 # Make list as response to 'timeserie' request
#                 if target['type'] == 'timeserie':
#                     for pd_check in pd_checks:
#                         if target['target'] == pd_check.name:
#                             response_data_timeserie = {
#                                 "target": pd_check.name,
#                                 "datapoints": [
#                                     [pd_check.status, int(pd_check.lasttesttime) * 1000]
#                                 ]
#                             }
#                             response.append(response_data_timeserie)
#                 # Make response on 'table' request
#                 elif target['type'] == 'table':
#                     for pd_check in pd_checks:
#                         if re.match(target['target'], pd_check.name):
#                             if pd_check.status == 'up':
#                                 pd_check_status = 1
#                             elif pd_check.status == 'down':
#                                 pd_check_status = 0
#                             else:
#                                 pd_check_status = pd_check.status
#                             response_data_table['rows'].append([pd_check.name, pd_check_status])
#                     response.append(response_data_table)
#                 # Make answer for test request
#                 elif target['type'] == 'test':
#                     response = {'message': 'TEST PASSED'}
#                 else:
#                     raise falcon.HTTPBadRequest(description='Unknown target type')

#             logger.debug('Response: ' + str(response))
#             resp.media = response
#             resp.status = falcon.HTTP_200

#         except falcon.HTTPBadRequest as BadRequestException:
#             logger.error('400 Client Error: Bad Request')
#             raise BadRequestException
#         except Exception as e:
#             logger.error('500 Internal Server Error: ' + str(e))
#             raise falcon.HTTPInternalServerError(description=str(e))


# class TestResource(object):
#     def on_get(self, req, resp):
#         test_response = {u'message': u'Hello world!'}
#         resp.media = test_response
#         resp.status = falcon.HTTP_200


api = application = falcon.API()

api.add_route('/', RootResource())
api.add_route('/weather', WeatherResource())
# api.add_route('/test', TestResource())
