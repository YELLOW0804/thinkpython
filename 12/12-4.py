def all_anagram(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        l = list(word)
        l.sort()
        delimiter = ''
        t = delimiter.join(l)
        if t in d:
            d[t].append(word)
        else:
            d[t] = [word]    
    return d

d = all_anagram('words.txt')
'''t = []
for n in d.values():
    if len(n) > 1:
        t.append(n)
t.sort()
for x in t:
    print x
    if x[0] == 'deltas':
        break'''
'''t = []
for n in d.values():
    if len(n) > 1:
        t.append((len(n), n))
t.sort(reverse = True)
for l in t:
    print l[1]'''

'''
res = {}
for word, anagram in d.iteritems():
    if len(word) == 8:
        res[word] = anagram
t = []
for n in res.values():
    if len(n) > 1:
        t.append(n)
for l in t:
    print l
'''