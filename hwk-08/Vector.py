class vector:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        res = ''

        for i in self.list:
            res += f'{i}:'

        return res[0:-1]

    def __add__(self, argList):
        res = []

        if type(argList) is vector:
            arg = str(argList).split(':')
        else:
            arg = argList

        for k, v in enumerate(arg):
            res.append(int(v) + self.list[k])

        return vector(res)

    __radd__ = __add__
