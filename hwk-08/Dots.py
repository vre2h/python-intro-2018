import decimal
import math


class Dots:

    def __init__(self, start, stop):
        self.start = float(start)
        self.stop = float(stop)

    def __getitem__(self, keys):
        if type(keys) is int:
            step = (self.stop-self.start) / (keys - 1)
        elif keys.step == None:
            step = (self.stop-self.start) / (keys.stop - 1)
        else:
            step = (self.stop-self.start) / (keys.step - 1)

        if type(keys) is int:
            return (self.start + i * step for i in range(keys))
        elif keys.step == None:
            return self.start + keys.start * step
        else:
            return (self.start + i * step for i in range(keys.start if keys.start else 0, keys.stop if keys.stop else keys.step))
