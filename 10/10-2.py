def capitalize_all(s):
    res = []
    for l in s:
        print l.capitalize()
        res.append(l.capitalize())
    return res

def capitalize_nested(l):
    res = []
    for i in l:
        res.append(capitalize_all(i))
    return res

l = [['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow']]

print capitalize_nested(l)