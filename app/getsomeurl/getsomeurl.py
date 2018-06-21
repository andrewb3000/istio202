from flask import Flask
from flask import abort
from flask import request
import requests
import os
# import time

REQUEST_URL=os.environ['REQUEST_URL']

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "GET App"

@app.route("/", methods=['GET'])
def getsomeurl():
    headers = dict(request.headers)
    # headers.pop('Host', None)
    del headers['Host']
    # app.logger.warn('Headers: %s', headers)
    try:
        get_response = requests.get(REQUEST_URL, headers=headers)
        if get_response.status_code == 200:
            return get_response.content
        else:
            abort(get_response.status_code)
    except Exception as e:
        abort(500)
