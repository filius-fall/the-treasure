from flask import Flask,request,jsonify

from .api_data import api_json_values


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return 'Hello world'


@app.route('/api/v1/data/all',methods=['GET'])
def api_data_all():
    return jsonify(api_json_values)

@app.route('/api/v1/data/',methods=['GET'])
def api_data_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No id found'
    
    values = []

    for data in api_json_values:
        if id == data['id']:
            values.append(data)

    return jsonify(values)