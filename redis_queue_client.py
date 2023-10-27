import redis

from redis_queue import RQueue
from tasks import get_word_counts


NUMBER_OF_TASKS = 10


if __name__ == "__main__":
    r = redis.Redis()
    queue = RQueue(conn=r, name="Test")
    count = 0
    for num in range(NUMBER_OF_TASKS):
        queue.enqueue(get_word_counts, "pride-and-prejudice.txt")
        queue.enqueue(get_word_counts, "heart-of-darkness.txt")
        queue.enqueue(get_word_counts, "frankenstein.txt")
        queue.enqueue(get_word_counts, "dracula.txt")
        count += 4
    print(f"Enqueued {count} tasks!")
