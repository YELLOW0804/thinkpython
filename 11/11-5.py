def histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

def invert_dict(d):
    invert = dict()
    for key in d:
        invert.setdefault(d[key], []).append(key)
    return invert

h = histogram('aabbcccddddee')
ih = invert_dict(h)
print ih
