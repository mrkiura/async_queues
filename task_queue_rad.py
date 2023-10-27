import multiprocessing
import time


from tasks import get_word_counts

PROCESSES = multiprocessing.cpu_count() - 1
NUMBER_OF_TASKS = 10


def process_tasks(task_queue):
    while not task_queue.empty():
        book = task_queue.get()
        get_word_counts(book)
    return True
