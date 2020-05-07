import collections


class Log:
    def __init__(self, size):
        self.size = size
        self.logs = []
        self.currentIdx = 0

    def record(self, order_id):
        self.logs[self.currentIdx] = order_id
        self.currentIdx += 1

    def get_last(self, i):
        return self.logs[i]

    def length_logs(self):
        return len(self.logs)


class LogWithCircularBuffer:
    def __init__(self, size):
        self.size = size
        self.logs = collections.deque(maxlen=self.size)

    def record(self, order_id):
        try:
            self.logs.append(order_id)
        except AttributeError:
            self.logs = collections.deque([0.] * self.size, maxlen=self.size)

    def get_last(self, i):
        try:
            return self.logs.index(i)
        except ValueError:
            return None

    def length_logs(self):
        return len(self.logs)
