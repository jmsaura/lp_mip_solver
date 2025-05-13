import unittest
from buggy_solver import solve_buggy_lp

class TestLPSolver(unittest.TestCase):
    def test_simple_lp(self):
        result = solve_buggy_lp()
        self.assertEqual(result["objective"], 20)
        self.assertEqual(result["x"], 0)
        self.assertEqual(result["y"], 0)

if __name__ == "__main__":
    unittest.main()