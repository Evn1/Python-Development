from types import GeneratorType


class Unique(object):
    def __init__(self, items, **kwargs):
        ignore_case = kwargs.get('ignore_case')
        if ignore_case is None:
            ignore_case = False
        self.res = []
        self.ignore_case = ignore_case
        if isinstance(items, GeneratorType):
            self.items = items
        else:
            self.items = iter(items)
        pass

    def __next__(self):
        self.this_el = self.items.__next__()
        if self.ignore_case:
            self.this_el = self.this_el.lower()
        if self.this_el in self.res:
            self.__next__();
        else:
            self.res.append(self.this_el)
        return self.this_el
        pass

    def __iter__(self):
        return self


data1 = ['a', 'A', 'b', 'B']
#print(
#   [x for x in Unique(data1, ignore_case=True)],
#   sep='\n')
