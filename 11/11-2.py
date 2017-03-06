def histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

word = 'abcddcbay'
d = histogram(word)
print d