import unittest
import io
from contextlib import redirect_stdout
from problem_330 import is2_cnf_satisfiable


class Problem330TestCase(unittest.TestCase):
    n_1 = 5
    m_1 = 7
    a_1 = [1, -2, -1, 3, -3, -4, -3]
    b_1 = [2, 3, -2, 4, 5, -5, 4]

    n_2 = 2
    m_2 = 3
    a_2 = [1, 2, -1]
    b_2 = [2, -1, -2]

    n_3 = 2
    m_3 = 4
    a_3 = [1, -1, 1, -1]
    b_3 = [2, 2, -2, -2]

    def test_is2_cnf_satisfiable_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            is2_cnf_satisfiable(self.n_1, self.m_1, self.a_1, self.b_1)
        out = f.getvalue()

        self.assertIn("satisfiable", out)

    def test_is2_cnf_satisfiable_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            is2_cnf_satisfiable(self.n_2, self.m_2, self.a_2, self.b_2)
        out = f.getvalue()

        self.assertIn("unsatisfiable", out)

    def test_is2_cnf_satisfiable_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            is2_cnf_satisfiable(self.n_3, self.m_3, self.a_3, self.b_3)
        out = f.getvalue()

        self.assertIn("satisfiable", out)


if __name__ == "__main__":
    unittest.main()
