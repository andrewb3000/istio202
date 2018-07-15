from flask import Flask
from flask import abort
from flask import request
from flask import jsonify
import requests
import os
# import time

REQUEST_URL=os.environ['REQUEST_URL']

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "GET App"

def getForwardHeaders(request):
    headers = {}

    user_cookie = request.cookies.get("user")
    if user_cookie:
        headers['Cookie'] = 'user=' + user_cookie

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            #print "incoming: "+ihdr+":"+val

    return headers


@app.route("/", methods=['GET'])
def getsomeurl():
    # print(request.query_string)
    format = request.args.get('format')
    # app.logger.warn('Format: %s', format)
    headers_all = dict(request.headers)
    # del headers_all['Host']
    app.logger.warn('Upstream Headers: %s', headers_all)
    headers = getForwardHeaders(request)
    # app.logger.warn('Downstream headers: %s', headers)
    try:
        get_response = requests.get(REQUEST_URL, headers=headers)
        if get_response.status_code == 200:
            # app.logger.warn('Reply headers: %s', get_response.headers)
            if 'application/json' in get_response.headers['Content-Type'] and format == 'json':
                return jsonify(get_response.json())
            else:
                return get_response.content
        else:
            abort(get_response.status_code)
    except Exception as e:
        abort(500)

@app.route("/noheaders", methods=['GET'])
def getsomeurl_noheaders():
    # print(request.query_string)
    format = request.args.get('format')
    headers_all = dict(request.headers)
    # del headers_all['Host']
    app.logger.warn('Headers: %s', headers_all)
    try:
        get_response = requests.get(REQUEST_URL)
        if get_response.status_code == 200:
            if get_response.headers['Content-Type'] == 'application/json' and format == 'json':
                return jsonify(get_response.json())
            else:
                return get_response.content
        else:
            abort(get_response.status_code)
    except Exception as e:
        abort(500)
