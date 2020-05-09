import unittest
from problem_17 import LogWithCircularBuffer, Log


class Problem16TestCase(unittest.TestCase):
    element = 1
    size_1 = 10
    size_2 = 5

    log_1 = Log(size_1)
    log_2 = Log(size_2)

    log_3 = LogWithCircularBuffer(size_1)
    log_4 = LogWithCircularBuffer(size_2)

    def test_record_1(self):
        [self.log_1.record(order_id) for order_id in range(self.size_1)]
        self.assertEqual(self.size_1, self.log_1.length_logs())

    def test_record_2(self):
        [self.log_2.record(order_id) for order_id in range(self.size_2)]
        self.assertEqual(self.size_2, self.log_2.length_logs())

    def test_record_3(self):
        [self.log_3.record(order_id) for order_id in range(self.size_1)]
        self.assertEqual(self.size_1, self.log_3.length_logs())

    def test_record_4(self):
        [self.log_4.record(order_id) for order_id in range(self.size_2)]
        self.assertEqual(self.size_2, self.log_4.length_logs())

    def test_get_last_1(self):
        [self.log_1.record(order_id) for order_id in range(self.size_2)]
        self.assertEqual(2, self.log_1.get_last(2))

    def test_get_last_2(self):
        [self.log_3.record(order_id) for order_id in range(self.size_1)]
        self.assertEqual(6, self.log_3.get_last(6))


if __name__ == "__main__":
    unittest.main()