def middle(l):
    res = []
    res = l[:]

    res.pop()
    res.pop(0)
    return res

l = [1, 2, 3, 4, 5, 6]

print middle(l)
print l
    
    