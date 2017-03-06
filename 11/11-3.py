def histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

def print_hist(h):
    l = h.keys()
    for c in h:
        print c, h[c]
    print '-----------'
    for d in l:
        print d, h[d]

h = histogram('yellow')
print_hist(h)