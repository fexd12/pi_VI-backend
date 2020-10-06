
import redis
from rq import Connection,Worker
redis_url = ''
redis_conn = redis.from_url(redis_url)
with Connection(redis_conn):
        worker = Worker('default')
        worker.work()
