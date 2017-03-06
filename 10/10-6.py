def is_sorted(t):
    index = 0
    while index < len(t) - 1:
        if t[index] > t[index + 1]:
            return False
        index += 1
    return True

def is_sorted_for(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
    return True

l = [1, 2, 3, 4, 5, 6]

print is_sorted(l)

