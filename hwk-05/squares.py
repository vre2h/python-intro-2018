def squares(w, h, *rest):
    mx = ['.'] * h

    for i in range(h):
        mx[i] = ['.'] * w

    for (X, Y, s, c) in rest:
        for j in range(s):
            for i in range(s):
                mx[Y + j][X + i] = c

    for i in mx:
        print(''.join(str(item) for item in i))
