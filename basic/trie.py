class TrieNode:
    def __init__(self):
        self.next_chars = [None for i in range(26)]
        self.is_end = False
