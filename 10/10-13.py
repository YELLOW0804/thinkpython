def wordlist():
    fin = open('9\\words.txt')
    res = []
    for word in fin:
        res.append(word.strip())
    return res

def bisect_new(t, n):
    low = 0
    high = len(t) - 1
    while low <= high:
        mid = (low + high) / 2
        m = t[mid]
        if m < n:
            low = mid + 1
        elif m > n:
            high = mid - 1
        else:
            return True
    return False



words = wordlist()
count = 0
def interlocking(t, word):
    word_one = word[::2]
    word_two = word[1::2]
    return bisect_new(t, word_one) and bisect_new(t, word_two)

for word in words:
    if interlocking(words, word):
        count += 1
print count
