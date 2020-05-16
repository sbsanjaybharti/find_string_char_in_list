
import time
import random
import string
from src.filter import Finder

if __name__ == '__main__':
    string_list = ['ddw', 'djd', 'dsds', 'ddw', 'fur', 'juk', 'sdfs', 'ssss', 'gh', 'dd', 'djd', 'dsds',\
                   'ddw', 'furd', 'juk', 'sdfs', 'ssss', 'gh', 'dd', 'djd', 'dsds', 'ddw', 'fur', 'juk',\
                   'dd', 'djdss', 'dsdsss', 'dema', 'sdfr', 'wq', 'sdfs', 'ssss', 'erdfw', 'vgfdr', 'ssss', 'bhgfr']
    t1 = time.time()
    finder = Finder(string_list)
    print(finder.find('sady'))
    print(finder.find('made'))
    print(finder.find('same'))
    print(finder.find('came'))
    print(finder.find('made'))
    print(finder.find('same'))
    print(finder.find('came'))
    print(finder.find('made'))
    print(finder.find('same'))
    print(finder.find('came'))
    print(finder.find('made'))
    print(finder.find('same'))
    print(finder.find('came'))
    print(finder.find('made'))
    print(finder.find('same'))
    print(finder.find('came'))
    print(finder.find('made'))
    print(finder.find('same'))
    print(finder.find('came'))
    print(finder.find('made'))
    print(finder.find('same'))
    print(finder.find('came'))
    t2 = time.time()

    print('time: {}'.format(t2-t1))
