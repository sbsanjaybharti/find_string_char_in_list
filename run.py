import string
from src.filter import Finder

if __name__ == '__main__':
    string_list = ["asd", "asdd", "fre", "glk", "lkm", "stdo"]
    
    finder = Finder(string_list)
    print(finder.find('sad'))

