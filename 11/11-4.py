def histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_ex(d, v):
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)
    return keys

h = histogram('aabbcccddddee')
print reverse_lookup_ex(h, 2)
print reverse_lookup_ex(h, 5)
