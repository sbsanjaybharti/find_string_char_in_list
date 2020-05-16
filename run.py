
import time
import random
import string
from src.filter import Finder

if __name__ == '__main__':
    string_list = ["asd", "asdd", "fre", "glk", "lkm", "stdo"]
    t1 = time.time()
    finder = Finder(string_list)
    print(finder.find('sad'))
    t2 = time.time()

    print('time: {}'.format(t2-t1))
