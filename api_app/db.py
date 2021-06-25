import redis
from flask import g


def get_db():
    if 'db' not in g:
        g.db = redis.StrictRedis(decode_responses = True)
    
    return g.db