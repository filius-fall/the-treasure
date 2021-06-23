import redis 

r = redis.StrictRedis()

r.hmset('user',dict(user='user',password='pass'))
