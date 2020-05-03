import unittest
import threading
import time
from problem_10 import job_scheduler, Scheduler


def f():
    print('thread function running')
    return


class Problem10TestCase(unittest.TestCase):
    n = 1

    # to be fixed with time.sleep
    def test_job_scheduler(self):
        thread = threading.Timer(self.n, f).start()
        self.assertEqual(thread, job_scheduler(f, self.n))

    def test_scheduler(self):
        scheduler = Scheduler().delay(f, self.n)
        thread = threading.Timer(self.n, f).start()
        self.assertEqual(thread, scheduler)


if __name__ == "__main__":
    unittest.main()
