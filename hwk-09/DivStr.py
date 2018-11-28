class DivStr(str):
    def __init__(self, string):
        self.str = string

    def __floordiv__(self, substrCount):
        length = len(self.str)
        extra = length // substrCount

        return (self.str[i:i + substrCount] for i in range(0, length - extra + 1, substrCount))

    def __mod__(self, n):
        length = len(self.str)
        extra = length % n
        return self.str[length - extra:]
