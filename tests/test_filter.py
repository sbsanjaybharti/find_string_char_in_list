import unittest
from src.filter import Filter


# #############################################################
# Test class for Filter class
# #############################################################
class TestFilter(unittest.TestCase):
    def setup(self):
        self.finder = Filter()

    # Negative Testing 1
    def test_data_empty(self):
        self.finder = Filter()
        data = self.finder.size()
        self.assertEqual(data, 0)

    # Positive Testing 1
    def test_data_exist(self):
        self.finder = Filter(['a', 'b', 'a'])
        data = self.finder.size()
        self.assertNotEqual(data, 0)

    # Negative Testing 1
    def test_process_data_empty(self):
        self.finder = Filter()
        data = self.finder.process()
        self.assertListEqual(data, [])

    # Positive Testing 1
    def test_process_data_singlelist(self):
        self.finder = Filter(['a', 'b', 'a'])
        data = self.finder.process()
        self.assertNotEqual(data, 0)

    # Positive Testing 2
    def test_process_data_multipleList(self):
        self.finder = Filter(['a', 'b', 'a', 'ab', 'cd', 'abc', 'xyz'])
        data = self.finder.process()
        self.assertNotEqual(data, 0)