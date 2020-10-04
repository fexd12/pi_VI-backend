
import redis
from rq import Connection,Worker
redis_url = 'redis://34.95.161.20:6379'
redis_conn = redis.from_url(redis_url)
with Connection(redis_conn):
        worker = Worker('default')
        worker.work()
