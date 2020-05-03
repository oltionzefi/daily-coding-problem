import threading
from time import time


def job_scheduler(f, n):
    return threading.Timer(n * time() * 1000, f).start()


class Scheduler:
    def __init__(self):
        # tuple (fn, time)
        self.fns = []
        # Locking for no changing fns at same time
        self.lock = threading.RLock()
        # waiting threads
        self.condition = threading.Condition(self.lock)

        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000

            with self.lock:
                # no addition to fns
                to_run = [fn for fn, due in self.fns if due <= now]
                self.fns = [(fn, due) for (fn, due) in self.fns if due > now]

            for fn in to_run:
                fn()

            with self.lock:
                if not self.fns:
                    # wait for new job
                    self.condition.wait()
                else:
                    ms_remaining = min(due for fn, due in self.fns) - time() * 1000
                    if ms_remaining > 0:
                        self.condition.wait(ms_remaining/1000)

    def delay(self, f, n):
        with self.lock:
            self.fns.append((f, time() * 1000 + n))
            # if scheduler is waiting then notify_all() to wake it up
            self.condition.notify_all()
