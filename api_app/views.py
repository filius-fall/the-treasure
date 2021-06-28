from flask import Flask,request,jsonify,render_template,g
import requests
from .api_data import api_json_values,external_data
from .db import get_db

import json

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





@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/api/v2/data/all',methods=['GET'])
def api_all():
    k = get_data()
    return jsonify(k)



@app.route('/api/v2/til_page',methods=["POST"])
def external_data_post():
    if 'password'  not in request.args or request.args['password'] != 'password':
        return "You are not authorised"

    request_data = request.get_json()

    
    title = request_data['title']
    url = request_data['url']
    descryption = request_data['descryption']


    
    user_id = str(g.db.incrby('next_user_id',1000))


    g.db.hset('user:' + user_id,'title',title)
    g.db.hset('user:' + user_id,'url',url)
    g.db.hset('user:' + user_id,'descryption',descryption)

    
    g.db.lpush('users',user_id)
    g.db.hset('user:' + user_id, 'id',user_id)

        


    return jsonify([title,url,descryption])

def get_data():
    
    user_list = g.db.lrange('users',0,-1)
    print(user_list)
    data_list = []
    for i in user_list:
        data = g.db.hgetall('user:' + i)
        print(data)
        data_list.append(data)

    return data_list




@app.route('/about')
def about():
    return render_template('about.html')

