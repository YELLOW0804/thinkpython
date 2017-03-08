memo = {}
memo[''] = ['']
def make_word_dict(filename):
    d = {}
    fin = open(filename)
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    for letter in ['i', 'a', '']:
        d[letter] = letter
    return d

def child_word(word, word_dict):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i + 1:]
        if child in word_dict:
            res.append(child)
    return res

def is_reducible(word, word_dict):
    if word in memo:
        return memo[word]
    res = []
    for child in child_word(word, word_dict):
        t = is_reducible(child, word_dict)
        if t:
            res.append(child)
    memo[word] = res
    return res

def all_reducible(word_dict):
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res

word_dict = make_word_dict('words.txt')
l = all_reducible(word_dict)
print len(l)

