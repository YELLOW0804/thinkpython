def chop(l):
    l.pop(0)
    l.pop()
    return l

l = [1, 2, 3, 4, 5, 6]

print chop(l)
