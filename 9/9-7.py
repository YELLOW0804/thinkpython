def is_three_double(word):
    i = 0
    j = 0
    while i < len(word) - 1:
        if word[i + 1] == word[i]:
            j = i + 2
            if len(word[j:]) > 4:
                if word[j] == word[j + 1]:
                    k = j + 2
                    if len(word[k:]) > 2:
                        if word[k] == word[k + 1]:
                            return True
        i += 1
    return False

def is_three_double_new(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i + 1] == word[i]:
            count += 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i += 1
    return False


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters."""
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return 

fin = open('9\words.txt')

count = 0
for word in fin:
    if is_three_double_new(word):
        print word
#print is_three_double('accssiibilities')
#print is_triple_double('accssiibilities')