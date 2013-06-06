import redis
import os

r = redis.StrictRedis(host=os.getenv("WERCKER_REDIS_HOST"), port=6379, db=0)
print r.info()

r.set('foo', 'bar')
result = r.get('foo')
assert result == 'bar'
print result
