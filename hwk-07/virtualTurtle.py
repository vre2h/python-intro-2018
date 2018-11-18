def turtle(coord, dir):
    x, y = coord

    while(True):
        side = yield x, y

        if side == 'l':
            dir += 1
            if dir > 3:
                dir = 0
        elif side == 'r':
            dir -= 1
            if dir < 0:
                dir = 3
        else:
            x, y = move(x, y, dir)


def move(x, y, dir):
    dirs = ['right', 'top', 'left', 'bottom']

    if dirs[dir] == 'top':
        return x, y + 1
    elif dirs[dir] == 'left':
        return x - 1, y
    elif dirs[dir] == 'bottom':
        return x, y - 1
    else:
        return x + 1, y
