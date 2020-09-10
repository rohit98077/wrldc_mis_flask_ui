'''
This is the web server that acts as a service that creates outages raw data
'''
from src.appConfig import getConfig
from flask import Flask, request, jsonify, render_template
from src.services.rawOutagesCreationHandler import RawOutagesCreationHandler
from src.services.rawPairAnglesCreationHandler import RawPairAnglesCreationHandler
from src.services.rawFreqCreationHandler import RawFrequencyCreationHandler
from src.services.rawVoltCreationHandler import RawVoltageCreationHandler
from src.services.derFreqCreationHandler import DerivedFrequencyCreationHandler
import datetime as dt
# from waitress import serve

app = Flask(__name__)

# get application config
appConfig = getConfig()

# Set the secret key to some random bytes
app.secret_key = appConfig['flaskSecret']


@app.route('/')
def hello():
    return render_template('home.html.j2')


@app.route('/createRawOutages', methods=['GET', 'POST'])
def createRawOutages():
    # in case of post request, create raw outages and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        outagesCreator = RawOutagesCreationHandler(
            appConfig['rawOutagesCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = outagesCreator.createRawOutages(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createRawOutages.html.j2')


@app.route('/createRawPairAngles', methods=['GET', 'POST'])
def createRawPairAngles():
    # in case of post request, create raw pair angles and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        pairAnglesCreator = RawPairAnglesCreationHandler(
            appConfig['rawPairAnglesCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = pairAnglesCreator.createRawPairAngles(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createRawPairAngles.html.j2')


@app.route('/createRawFreq', methods=['GET', 'POST'])
def createRawFreq():
    # in case of post request, create raw freq and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        rawFreqCreator = RawFrequencyCreationHandler(
            appConfig['rawFrequencyCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = rawFreqCreator.createRawFrequency(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createRawFreq.html.j2')


@app.route('/createRawVolt', methods=['GET', 'POST'])
def createRawVolt():
    # in case of post request, create raw voltage and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        rawVoltCreator = RawVoltageCreationHandler(
            appConfig['rawVoltageCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = rawVoltCreator.createRawVoltage(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createRawVolt.html.j2')


@app.route('/createDerFreq', methods=['GET', 'POST'])
def createDerFreq():
    # in case of post request, create derived frequency and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        derFreqCreator = DerivedFrequencyCreationHandler(
            appConfig['derivedFrequencyCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = derFreqCreator.createDerivedFrequency(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createDerFreq.html.j2')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
    # serve(app, host='0.0.0.0', port=int(appConfig['flaskPort']), threads=1)
