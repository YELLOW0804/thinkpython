def is_anagram(word_a, word_b):
    if len(word_a) != len(word_b):
        return False
    list_a = list(word_a)
    list_b = list(word_b)
    list_a.sort()
    list_b.sort()
    delimiter = ''
    s_a = delimiter.join(list_a)
    s_b = delimiter.join(list_b)
    
    return s_a == s_b

print is_anagram('1', '')