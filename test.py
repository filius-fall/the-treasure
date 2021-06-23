import redis 
from flask import g,Flask
from app.db import init_db

app = Flask(__name__)
r = redis.StrictRedis()

g.db = init_db()
# r.hmset('user',dict(user='rams',password='11'))

k = str(g.db.incrby('next_user_id',1000))
print(k)