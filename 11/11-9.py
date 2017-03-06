def has_duplicates_ex(t):
    return len(set(t)) < len(t)
    

def has_duplicates(t):
    for i in range(len(t) - 1):
        if t[i] in t[i + 1:]:
            return True
    return False

l = [1, 2, 3, 3, 4, 5]

print has_duplicates(l)
print has_duplicates_ex(l)