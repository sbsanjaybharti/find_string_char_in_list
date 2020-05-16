import collections

def singletonAvoidDuplicates(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

# Converting list in to group of string length
class Filter:
    def __init__(self, list_data=[]):
        self.list_data = list_data
        self.data = collections.defaultdict(list)

    def size(self):
        return len(self.list_data)

    def process(self):
        if self.size() != 0:
            for string in self.list_data:
                self.data[len(string)].append(string)
            return self.data
        else:
            return []

@singletonAvoidDuplicates
class Finder:
    def __init__(self, string_list=[]):
        """Get the list in the from of disc list where key will be the length of string"""
        if len(string_list) == 0:
            self.data = []
        else:
            self.data = Filter(string_list).process()

    def size(self):
        return len(self.data)

    def find(self, string=None):
        result = []
        if string is None:
            return "Finding string not provided"

        if len(string) in self.data:
            for element in self.data[len(string)]:
                if sorted(string) == sorted(element):
                    result.append(element)
        return result
