import pickle
import uuid


class RQueue:
    def __init__(self, conn, name) -> None:
        self.conn = conn
        self.name = name

    def enqueue(self, func, *args):
        task = RTask(func, *args)
        serialized_task = pickle.dumps(task, protocol=pickle.HIGHEST_PROTOCOL)
        self.conn.lpush(self.name, serialized_task)
        return task.id

    def dequeue(self):
        _, serialized_task = self.conn.brpop(self.name)
        task = pickle.loads(serialized_task)
        task.process_task()
        return task

    def __len__(self):
        return self.conn.llen(self.name)


class RTask:
    def __init__(self, func, *args) -> None:
        self.id = str(uuid.uuid4())
        self.func = func
        self.args = args

    def process_task(self):
        self.func(*self.args)
