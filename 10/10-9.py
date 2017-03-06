def remove_duplicates(t):
    res = []
    for i in t:
        if i not in res:
            res.append(i)
    return res

l = [6, 1, 2, 3, 4, 5, 3, 6]

print remove_duplicates(l)
