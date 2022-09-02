from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    file = open('data.json', 'w')
    return jsonify(json.load(file))

@app.route('/getreq')
def get_req():
    variable = request.get_json()
    file = open('data.json', 'w')
    json.dump(variable, file)
    file.close()
    return 'ok'

