import unittest

import run

class TestRun(unittest.TestCase):

    def test_execute(self):
      self.assertEqual(2, run.execute(1))
    def test_execute_minus(self):
      self.assertEqual(0, run.execute(-1))

if __name__ == '__main__':
    unittest.main()
