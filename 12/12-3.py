def most_frequent(word):
    d = {}
    for letter in word:
        d = make_histogram(word)
    temp = []
    for l, f in d.items():
        temp.append((f, l))
    temp.sort()
    res = []
    for l, f in temp:
        res.append(f)
    return res


def make_histogram(word):
    d = {}
    for letter in word:
        d[letter] = d.get(letter, 0) + 1
    return d

strs = open('words.txt').read(50)
print most_frequent(strs)
