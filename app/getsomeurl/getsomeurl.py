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

@app.route("/")
def getsomeurl():
    headers = dict(request.headers)
    # headerss.pop('Host', None)
    del headers['Host']
    # app.logger.warn('Headers: %s', headerss)
    try:
        time = requests.get(REQUEST_URL, headers=headers)
        if time.status_code == 200:
            return time.content
        else:
            abort(time.status_code)
    except Exception as e:
        abort(500)
