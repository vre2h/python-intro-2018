class we:
    count = 0

    def __init__(self, *args):
        we.count += 1

    def __del__(self, *args):
        we.count -= 1
