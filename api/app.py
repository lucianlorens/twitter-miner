import datetime
import sys
import os

from flask import Flask, request, jsonify, Response, send_from_directory, send_file

from flasgger import Swagger
from flasgger import swag_from
from swagger.swagger_config import swagger_configuration

abs_path = os.path.dirname(os.path.realpath(__file__))
abs_path = abs_path.replace("api", "job")

sys.path.append(abs_path)

import runner

app = Flask(__name__)
swagger = Swagger(app, config=swagger_configuration)

@app.route('/healthcheck', methods=['GET'])
@swag_from('swagger/healthcheck.yml')
def test():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    return jsonify({'status': 'ok'})


@app.route('/trigger', methods=['GET'])
@swag_from('swagger/trigger.yml')
def trigger():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    data = runner_.run_job()
    return jsonify(data)


@app.route('/status', methods=['GET'])
@swag_from('swagger/status.yml')
def status():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    data = runner_.status()
    return jsonify(data)


@app.route('/stop', methods=['GET'])
@swag_from('swagger/stop.yml')
def stop():
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    data = runner_.stop_job()
    return jsonify(data)


@app.route('/download', methods=['GET', 'POST'])
#TODO implement download route to swagger.
#@swag_from('swagger/download.yml')
def download():
    #TODO Improve this function.
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    tsv_file = runner_.download()
    print("/../"+tsv_file)
    app.logger.info(tsv_file)
    return send_from_directory('../', tsv_file, as_attachment=True, attachment_filename='output.tsv')
    #return send_file("../"+tsv_file, attachment_filename='output.tsv')
"""
"""

"""
#TODO Implement result route and swagger
#show raw data on the browser 
#implement mode of showing on browser the .tsv 
@app.route('/result', methods=['GET'])
@swag_from('swagger/result.yml')
def result():
    #
    print("Request on {} route at".format(request.url_rule), datetime.datetime.now())
    runner_ = runner.SingleRunner()
    tsv_file = runner_.download()
    print("/../"+tsv_file)
    app.logger.info(tsv_file)
    return send_from_directory('../', tsv_file, as_attachment=True, attachment_filename='output.tsv')
    #return send_file("../"+tsv_file, attachment_filename='output.tsv')
"""