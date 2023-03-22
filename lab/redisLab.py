import redis


REDIS_PASSWORD = "plZdYk4XnNWaS9GgRlVOWm-39ZqvWVAg-cawCdtZndBUNciDQ1"
pool = redis.ConnectionPool(host='192.168.56.90', port=6379, decode_responses=True, password=REDIS_PASSWORD)
r = redis.Redis(connection_pool=pool)

def event_handler(msg):
    print('Handler', msg)

def subscribe():
    pubsub = r.pubsub()
    subscribe_key = '*'
    pubsub.psubscribe(**{subscribe_key: event_handler})
    pubsub.run_in_thread(sleep_time=.01)

if __name__ == '__main__':
    subscribe()