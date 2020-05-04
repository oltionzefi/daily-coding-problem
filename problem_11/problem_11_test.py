import unittest
from problem_11 import TrieDataStructure


class Problem11TestCase(unittest.TestCase):
    list1 = ["dog", "deer", "deal"]
    search_term_1 = "de"
    search_term_2 = "deer"

    list2 = ["things", "something", "other", "nothing"]
    search_term_3 = "thing"
    search_term_4 = "nope"

    trie_data_structure_1 = TrieDataStructure()
    for value in list1:
        trie_data_structure_1.insert(value)

    trie_data_structure_2 = TrieDataStructure()
    for value in list2:
        trie_data_structure_2.insert(value)

    def test_search_1(self):
        search_list = self.trie_data_structure_1.search(self.search_term_1)
        self.assertEqual(["deer", "deal"], search_list)

    def test_search_2(self):
        search_list = self.trie_data_structure_1.search(self.search_term_2)
        self.assertEqual(["deer"], search_list)

    def test_search_3(self):
        search_list = self.trie_data_structure_2.search(self.search_term_3)
        self.assertEqual(["things", "something", "nothing"], search_list)

    def test_search_4(self):
        search_list = self.trie_data_structure_2.search(self.search_term_4)
        self.assertEqual(None, search_list)


if __name__ == "__main__":
    unittest.main()