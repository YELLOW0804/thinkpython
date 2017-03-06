def uses_only(word, letters):
    for line in word:
        if not (line in letters):
            return False
    return True



    
