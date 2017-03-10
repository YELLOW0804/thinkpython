import string
import random
import bisect

def process_line(line, his):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        his[word] = his.get(word, 0) + 1

def spik_head(fin):
    for line in fin:
        if line.startswith('*END*THE SMALL PRIN'):
            break

def process_file(filename, is_skip = True):
    his = {}
    fin = open(filename)
    if is_skip:
        spik_head(fin)
    for line in fin:
        process_line(line, his)
    return his

filename = 'emma.txt'

#The number of each word in a dictionary 
d = process_file(filename)

#Total number of words 
total = sum(d.values())
print total, len(d)

#The 20 most frequently used words
l = []
for word, num in d.items():
    l.append((num, word))
l.sort(reverse=True)
#for i in l[:20]:
#    print i

def check_words(word, words):
    if word not in words:
        return word
    else:
        return 0
# list        
'''def wordlist():
    fin = open('words.txt')
    res = []
    for word in fin:
        res.append(word.strip())
    return res

l = wordlist()
res = []
for key in d:
    word = check_words(key, l)
    if word:
        res.append(word)'''

#dict
def sub_dict(d1, d2):
    ''' In d1, not in d2'''
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

#words = process_file('words.txt', is_skip = False)

#dif = sub_dict(d, words)

#for key in dif:
#    print key

#set
'''d_set = set(d.keys())
word_set = set(words)
s = d_set.difference(word_set)
print len(s)'''

#13-7
def random_word(h):
    res = []
    for key, num in h.items():
        res.extend([key] * num)
    return random.choice(res)
#print random_word(d)

def total_ex(l):
    res = []
    sum = 0
    for s in l:
        sum += s
        res.append(sum)
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
    return 0

def random_wors_ex(h):
    keys = h.keys()
    l = total_ex(h.values())
    index = random.randint(0, l[len(l) - 1] - 1)
    res_index = bisect.bisect(l, index)
    return keys[res_index]

for i in range(10):
    print random_wors_ex(d)

def random_word(hist):
    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect.bisect(freqs, x)
    return words[index]
#for i in range(10):
#    print random_word(d)