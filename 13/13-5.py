import random
def histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

def choose_from_hist(his):
    res = ''
    l = []
    for key, val in his.items():
        for i in range(val):
            l.append(key) 
    return random.choice(l)

h = histogram('aabbcccddddeeeeeeeeeeeee')

for i in range(10):
    print choose_from_hist(h)