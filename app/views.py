from flask import Flask,render_template,request,g,current_app,session,redirect,url_for
from .db import init_db
import redis


app = Flask(__name__)
DEBUG = True

SECRET_KEY = '8cb049a2b6160e1838df7cfe896e3ec32da888d7'
app.secret_key = SECRET_KEY

def get_db():
    if 'db' not in g:
        g.db = redis.StrictRedis()
    
    return g.db

@app.before_request
def before_request():
    g.db = get_db()

@app.route('/',methods=['GET','POST'])
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
    g.db.hset('users',username,user_id)
    session['username'] = username
    return redirect(url_for('home'))

@app.route('/home',methods=['GET','POST'])
def home():
    posts = [{"usernme":"sreeram","time":"today","text":"Example test"}]
    return render_template('index.html',posts = posts)

@app.route('/logout',methods=['GET','POST'])
def logout():
    return 'Logout'