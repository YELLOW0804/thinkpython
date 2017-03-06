def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1: -1]

def is_plaindrome(word):
    length = len(word)
    if length <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_plaindrome(middle(word))

word = '1122332211'
print is_plaindrome(word)