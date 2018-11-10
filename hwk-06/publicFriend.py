def makeMetList():
    friends = {}
    allPeople = set()

    while(True):
        m, n = eval(input())

        if m == 0 and n == 0:
            break
        if m not in friends:
            friends[m] = set()
            allPeople.add(m)
        elif n not in friends:
            friends[n] = set()
            allPeople.add(n)
        else:
            friends[m].add(n)
            friends[n].add(m)

    return friends, allPeople


def publicFriend(friendsList, allPeople):
    res = []
    for every in friendsList:
        if allPeople - friendsList[every] == set([every]):
            res.append(every)
    return res


friends, allPeople = makeMetList()
print(*publicFriend(friends, allPeople))
