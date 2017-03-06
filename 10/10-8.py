import random
def has_duplicates(t):
    for i in range(len(t) - 1):
        if t[i] in t[i + 1:]:
            return True
    return False

def random_birthday(n):
    res = []
    for i in range(n):
        res.append(random.randint(1, 365))
    return res

count = 0
for j in range(1000):
    l = random_birthday(23)
    if has_duplicates(l):
        count += 1


print count / 1000.0


