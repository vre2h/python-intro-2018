def toint(f):
    def newF(*args):
        newArgs = ()

        for i in args:
            if type(i) is int or type(i) is float:
                newArgs = (*newArgs, int(i))
            else:
                newArgs = (*newArgs, i)

        res = f(*newArgs)

        if type(res) is int or type(res) is float:
            res = int(res)

        return res

    return newF
