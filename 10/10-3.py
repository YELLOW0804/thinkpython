def total_ex(l):
    res = []
    sum = 0
    for s in l:
        sum += s
        res.append(sum)
    return res

l = []
for i in range(100):
    l.append(i + 1)

print total_ex(l)

