'''
This is the web server that acts as a service that creates outages raw data
'''
from src.appConfig import getConfig
from flask import Flask, request, jsonify, render_template
# from waitress import serve

app = Flask(__name__)

# get application config
appConfig = getConfig()

# Set the secret key to some random bytes
app.secret_key = appConfig['flaskSecret']


@app.route('/')
def hello():
    return render_template('home.html.j2')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
    # serve(app, host='0.0.0.0', port=int(appConfig['flaskPort']), threads=1)