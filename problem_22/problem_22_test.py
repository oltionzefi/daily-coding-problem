import unittest
from problem_22 import original_sentence


class Problem22TestCase(unittest.TestCase):
    dict1 = ['quick', 'brown', 'the', 'fox']
    dict2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    string1 = "thequickbrownfox"
    string2 = "bedbathandbeyond"

    def test_original_sentence_1(self):
        self.assertEqual(['the', 'quick', 'brown', 'fox'], original_sentence(self.dict1, self.string1))

    def test_original_sentence_2(self):
        self.assertEqual(['bed', 'bath', 'and', 'beyond'], original_sentence(self.dict2, self.string2))
        # self.assertEqual(['bedbath', 'and', 'beyond'], original_sentence(self.dict2, self.string2))


if __name__ == "__main__":
    unittest.main()
