def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    s = ord(letter) - start
    res = (s + n) % 26 + start
    return chr(res)
    
def rotate(word, n):
    res = ''
    for l in word:
        res += rotate_letter(l, n)
    return res

def worddict():
    fin = open('words.txt')
    res = dict()
    for word in fin:
        res[word.strip()] = word.strip()
    return res

words = worddict()
print 'words dict is created'
print words

for word in words:
    for i in range(1, 26):
        if rotate(word.strip(), i) in words:
            print word,rotate(word, i)