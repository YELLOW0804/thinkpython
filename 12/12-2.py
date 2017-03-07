import random
def sort_by_length(words):
    tmp = []
    for word in words:
        tmp.append((len(word), word))
    tmp.sort()

    res = []
    for l, t in tmp:
        res.append(t)
    return res

def sort_by_length_random(words):
    tmp = []
    for word in words:
        tmp.append((len(word), random.random(), word))
    tmp.sort()

    res = []
    for l, r, t in tmp:
        res.append(t)
    return res
words = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michae', 'yellow']
print sort_by_length(words)
print sort_by_length_random(words)
