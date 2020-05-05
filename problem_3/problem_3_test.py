import unittest
from problem_3 import Node, deserialize, serialize


class Problem3TestCase(unittest.TestCase):
    set1 = []

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    unittest.main()