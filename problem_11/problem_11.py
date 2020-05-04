from basic import TrieNode


class TrieDataStructure:
    def __init__(self):
        self.root = TrieNode()
        self.word_dict = []

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.next_chars[ord(word[i]) - ord('a')]:
                node.next_chars[ord(word[i]) - ord('a')] = TrieNode()
            node = node.next_chars[ord(word[i]) - ord('a')]
        node.is_end = True

    def search(self, word):
        node = self.root
        for i in range(len(word)):
            if node.next_chars[ord(word[i]) - ord('a')]:
                node = node.next_chars[ord(word[i]) - ord('a')]
            else:
                self.word_dict = []
                return
        self.word_dict = []
        self.autocomplete_search(node, word)

    def autocomplete_search(self, node, word):
        if not word:
            return None
        if node.is_end:
            self.word_dict.append(word)
            return self.word_dict
        for i in range(26):
            if node.next_chars[i]:
                self.autocomplete_search(node.next_chars[i], word + chr(i + ord('a')))
