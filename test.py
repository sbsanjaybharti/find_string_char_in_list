import unittest

"""Runs the unit tests."""
tests = unittest.TestLoader().discover('tests', pattern='test*.py')
result = unittest.TextTestRunner(verbosity=2).run(tests)
if result.wasSuccessful():
    print(0)
print(1)
if __name__ == '__main__':
    unittest.main()

