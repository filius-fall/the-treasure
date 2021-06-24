from flask import Flask,render_template,request,g,current_app,session,redirect,url_for
from .db import init_db
import redis
from  datetime import date

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
    if request.method == 'GET':
        return render_template('login.html',error = error)
    
    username = request.form.get('username',False)
    password = request.form.get('username',False)
    print(username,password)
    user_id = str(g.db.hget('users',username),'utf-8')
    if not user_id:
        error = 'Wrong username'
        return render_template('login.html',error=error)
    saved_password = str(g.db.hget('user:' + user_id,'password'),'utf-8')
    if password != saved_password:
        error = "Wrong Password"
        return render_template('login.html',error=error)

    session['username'] = username

    return redirect(url_for('home'))



@app.route('/signup',methods=['GET','POST'])
def signup():
    
    error = None
    if request.method == 'GET':
        return render_template('signup.html',error = error)
    
    username = request.form.get('username',False)
    password = request.form.get('username',False)

    print('HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
    print(username,password)
    user_id = str(g.db.incrby('next_user_id',1000))
    g.db.hset('user:' + user_id,'username',username)
    g.db.hset('user:' + user_id,'password',password)
    # g.db.hmset('user:' + user_id,dict(username=username,password=password))
    g.db.hset('users',username,user_id)
    session['username'] = username
    return redirect(url_for('home'))

@app.route('/home',methods=['GET','POST'])
def home():
    if not session:
        return redirect(url_for('login'))
    user_id = g.db.hget('users', session['username'])
    if request.method == 'GET':
        return render_template('index.html', post=_get_post(user_id))
    text = request.form['post']
    post_id = str(g.db.incr('next_post_id'))
    g.db.hmset('post:' + post_id, dict(user_id=user_id,
                                       ts=date.today().strftime('%d-%m-%y'), text=text))
    g.db.lpush('posts:' + str(user_id), str(post_id))
    g.db.lpush('post:' + str(user_id), str(post_id))
    g.db.ltrim('post:' + str(user_id), 0, 100)
    return render_template('index.html', posts=_get_post(user_id))


@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

def _get_post(user_id):
    posts = g.db.lrange('post:' + str(user_id), 0, -1)
    print('YYYYYYYYYYYYYYYYYYYYYYYY_________________YYYYYYYYYYYYYYYYYYYYYYYY____________YYYYYYYYYYYYYYY')
    print(posts)
    post_array = []
    for post_id in posts:
        post = g.db.hgetall('post:' + str(post_id, 'utf-8'))        
        post_array.append(dict(username=g.db.hget('user:' + str(post[b'user_id'], 'utf-8'), 'username'),ts=post[b'ts'],text=post[b'text']))
    return post_array