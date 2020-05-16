import unittest
from src.filter import Finder

# #############################################################
# Test class for Finder class
# #############################################################
class TestFinder(unittest.TestCase):
    def setup(self):
        self.finder = Finder()

    def test_is_singleton(self):
        obj1 = Finder()
        obj2 = Finder()
        self.assertEqual(obj1, obj2)

    # Negative Testing 1
    def test_data_empty(self):
        self.finder = Finder()
        data = self.finder.size()
        self.assertEqual(data, 0)

    # Negative Testing 1
    def test_process_data_empty(self):
        self.finder = Finder()
        data = self.finder.find()
        self.assertEqual(data, "Finding string not provided")

    # Positive Testing 1
    def test_process_data_singlelist(self):
        self.finder = Finder(['a', 'b', 'a'])
        data = self.finder.find()
        self.assertNotEqual(data, 0)

    # Positive Testing 2
    def test_process_data_multipleList(self):
        self.finder = Finder(['a', 'b', 'a', 'ab', 'cd', 'abc', 'xyz'])
        data = self.finder.find()
        self.assertNotEqual(data, 0)


if __name__ == '__main__':
    unittest.main()

