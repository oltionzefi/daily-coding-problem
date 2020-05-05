class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    values = []

    def serializer(node):
        if not node:
            values.append('?')
        else:
            values.append(str(node.value))
            serializer(node.left)
            serializer(node.right)

    serializer(root)
    return ','.join(values)


def deserialize(string):
    values = iter(string.split(','))

    def deserializer():
        val = next(values)
        if val == '?':
            return None
        else:
            node = Node(int(val))
            node.left = deserializer()
            node.right = deserializer()
            return node

    return deserializer()
