import datetime
import sys
import os

from flask import Flask, request, jsonify
#from flasgger import Swagger
#from flasgger import swag_from

#from swagger.swagger_config import swagger_configuration

abs_path = os.path.dirname(os.path.realpath(__file__))
abs_path = abs_path.replace("api", "job")

sys.path.append(abs_path)

import runner

app = Flask(__name__)
#swagger = Swagger(app, config=swagger_configuration)

@app.route('/test', methods=['POST', 'GET'])
def test():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    return "TEST OK!"

@app.route('/trigger', methods=['POST', 'GET'])
def trigger():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    data = runner_.run_job()
    return jsonify(data)


@app.route('/status', methods=['POST', 'GET'])
def status():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    data = runner_.status()
    return jsonify(data)


@app.route('/stop', methods=['POST', 'GET'])
def stop():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    data = runner_.stop_job()
    return jsonify(data)

@app.route('/result', methods=['POST', 'GET'])
def result():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    data = runner_.download()
    return jsonify(data)
