import time
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
            return mid
    return -1

words = wordlist()
start = time.time()
print bisect_new(words[:10], 'a')
print time.time() - start

