import time
def wordlist():
    fin = open('9\\words.txt')
    res = []
    for word in fin:
        res.append(word.strip())
    return res
def wordlist_new():
    fin = open('9\\words.txt')
    res = []
    for word in fin:
        res += [word.strip()]
    return res

mark = time.time()
words = wordlist()
print time.time() - mark
print len(words)

mark = time.time()
words_new = wordlist_new()
print time.time() - mark
print len(words_new)
