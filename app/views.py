from flask import Flask,render_template,request,g,current_app,session,redirect,url_for
from .db import init_db


app = Flask(__name__)
DEBUG = True

@app.before_request
def before_request():
    g.db = init_db()

@app.route('/')
def login():
    error = None
    return render_template('login.html',error = error)

@app.route('/signup',methods=['GET','POST'])
def signup():
    
    error = None
    if request.method == 'GET':
        return render_template('signup.html',error = error)
    
    username = request.form['username']
    password = request.form['password']

    user_id = str(g.db.incrby('next_user_id',1000))
    g.db.hmset('user:' + user_id,dict(username=username,password=password))
    g.db.hget('users',username,user_id)
    session['username'] = username
    return redirect(url_for('home'))

@app.route('/home')
def home():
    posts = [{"usernme":"sreeram","time":"today","text":"Example test"}]
    return render_template('index.html',posts = posts)