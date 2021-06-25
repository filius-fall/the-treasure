from flask import Flask,request,jsonify,render_template,g

from .api_data import api_json_values,external_data
from .db import get_db

import json
import ast

app = Flask(__name__)
app.config["DEBUG"] = True
SECRET_KEY = '8cb049a2b6160e1838df7cfe896e3ec32da888d7'
app.secret_key = SECRET_KEY

@app.before_request
def before_request():
    g.db = get_db()

@app.route('/')
def index():
    data = get_data()

    return render_template('index.html',api_data=data)

@app.route('/test')
def test():
    return render_template('test.html')

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/api/v2/data/all',methods=['GET'])
def api_all():
    k = g.db.hgetall('user:test')
    return jsonify(k)



@app.route('/api/v2/external',methods=['GET',"POST"])
def external_data_post():
    if 'password'  not in request.args or request.args['password'] != 'password':
        return "You are not authorised"
    if 'data' in request.args:
        data = ast.literal_eval(request.args['data'])
    
    titles = ['title','url','descryption']
    user_id = str(g.db.incrby('next_user_id',1000))
    for i in titles:
        g.db.hset('user:' + user_id,i,data[i])

    
    g.db.lpush('users',user_id)
    g.db.hset('user:' + user_id, 'id',user_id)

        


    return jsonify(data)

def get_data():
    
    # titles = ['title','url','descryption']
    user_list = g.db.lrange('users',0,-1)
    print(user_list)
    data_list = []
    for i in user_list:
        data = g.db.hgetall('user:' + i)
        print(data)
        data_list.append(data)

    return data_list