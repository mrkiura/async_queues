import redis


from redis_queue import RQueue


def worker():
    r = redis.Redis()
    queue = RQueue(conn=r, name="Test")
    if len(queue) > 0:
        queue.dequeue()
    else:
        print("No tasks in the queue")


if __name__ == "__main__":
    worker()
