from flask import Flask
from flask import abort
import requests
import os
# import time

# REQUEST_URL=os.environ['RESOURCE_URL']

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "GET App"

@app.route("/")
def getsomeurl():
    try:
        time = requests.get(os.environ['REQUEST_URL'])
        if time.status_code == 200:
            return time.content
        else:
            abort(time.status_code)
    except Exception as e:
        abort(502)
