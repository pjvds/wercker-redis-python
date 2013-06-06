import redis
import os

host = os.getenv("WERCKER_REDIS_HOST")
port = os.getenv("WERCKER_REDIS_PORT")

r = redis.StrictRedis(host=, port=port, db=0)
print r.info()

r.set('foo', 'bar')
result = r.get('foo')
assert result == 'bar'
print result
