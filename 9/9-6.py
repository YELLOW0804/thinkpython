def is_abecedarian(word):
    '''i = 0
    while i < len(word) - 1:
        if word[i] > word[i + 1]:
            return False
        i += 1
    return True'''
    '''for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True'''
    '''previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True'''
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

print is_abecedarian('abcdefg')
