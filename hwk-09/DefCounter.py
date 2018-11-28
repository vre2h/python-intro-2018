from collections import Counter


class DefCounter(Counter):

    def __init__(self, *arg, missing=-1, **argn):
        self.current = Counter(argn) if argn else Counter(*arg)
        self.missing = missing

    def __missing__(self, key):
        return self.current[key] if self.current[key] else self.missing

    def __setitem__(self, key, value):
        self.current[key] += value

    def __str__(self):
        return f'DefCounter({dict(self.current)})'
