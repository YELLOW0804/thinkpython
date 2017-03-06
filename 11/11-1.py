import time
def wordlist():
    fin = open('words.txt')
    res = []
    for word in fin:
        res.append(word.strip())
    return res

def dict_test():
    words = wordlist()
    word_dic = dict()
    for word in words:
        word_dic[word] = len(word)
    return word_dic

d = dict_test()
start = time.time()
if  'yellow' in d:
    print d['yellow']
end = time.time() - start
print end
