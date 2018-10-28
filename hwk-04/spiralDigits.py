col, row = eval(input())


def lessNine(num):
    # checker for num's to be less than 9
    if num > 9:
        return 0
    return num


def spiralDig(col, row):
    # creating matrix col*row with -1 as values
    mx = ['-1'] * row

    for i in range(row):
        mx[i] = ['-1'] * col

    # we've 4 directions
    direction = ['right', 'bottom', 'left', 'top']
    directionCounter = 4

    # counter for digit from 0 - 9
    digit = 0
    count = 0

    # position of start
    x = 0
    y = 0

    while(count < row * col):
        if direction[directionCounter % 4] == 'right':
            while(y < col and mx[x][y] == '-1'):
                mx[x][y] = digit
                y += 1
                digit += 1
                digit = lessNine(digit)
            else:
                directionCounter += 1
                y -= 1
                x += 1

        if direction[directionCounter % 4] == 'bottom':
            while(x < row and mx[x][y] == '-1'):
                mx[x][y] = digit
                x += 1
                digit += 1
                digit = lessNine(digit)
            else:
                directionCounter += 1
                x -= 1
                y -= 1

        if direction[directionCounter % 4] == 'left':
            while(y >= 0 and mx[x][y] == '-1'):
                mx[x][y] = digit
                y -= 1
                digit += 1
                digit = lessNine(digit)
            else:
                directionCounter += 1
                y += 1
                x -= 1

        if direction[directionCounter % 4] == 'top':
            while(x >= 0 and mx[x][y] == '-1'):
                mx[x][y] = digit
                x -= 1
                digit += 1
                digit = lessNine(digit)
            else:
                directionCounter += 1
                x += 1
                y += 1
        count += 1

    for i in mx:
        print(' '.join(str(item) for item in i))


spiralDig(col, row)
