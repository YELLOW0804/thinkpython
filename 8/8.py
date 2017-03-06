
#8-1 test
#def reverse_print(s):
#    """ 8-1 """
#    for i in range(len(s)):
#        print s[len(s) - 1 - i]
#reverse_print('yellow')

#8-2 test
#prefixes = 'JKLMNOPQ'
#suffix = 'ack'

#for letter in prefixes:
#    if letter == 'O' or letter == 'Q':
#        print letter + 'u' + suffix
#    else:
#        print letter + suffix

#8-3
#fruit = 'yellow'
#print fruit[:]

#8-4
#def find(word, letter, n):
#    index = n
#    while index < len(word):
#        if word[index] == letter:
#            return index
#        index += 1
#    return -1

#word = 'zhangchi'
#print find(word, 'h', 2)

#8-5
#def count(word, letter):
#    count = 0
#    index = 0
#    while index < len(word):
#        if word[index] == letter:
#            count += 1
#        index += 1
#    return count

#print count('banana', 'a')

#8-6
#def count_new(word, letter):
#    count = 0
#    index = 0
#    while index < len(word):
#        if find(word, letter, index) >= 0:
#            count += 1
#            index = find(word, letter, index)
#        index += 1
#    return count
#print count_new('bananaaa', 'a')

#8-7
#word = 'banana'
#letter = 'a'
#print word.count(letter)

#8-9
#def is_reverse(word1, word2):
#    if len(word1) != len(word2):
#        return False
#    i = 0
    #j = len(word1)
#    j = len(word2) - 1

    #j > 0
#    while j > i:
#        if word1[i] != word2[j]:
#            return False
#        i += 1
#        j -= 1
#    return True
#print is_reverse('abcd', 'fcba')

#8-10
#def is_palindrome(s):
#    return s[::-1] == s

#print is_palindrome('123456543210')

#8-12

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

print rotate('a', 26)