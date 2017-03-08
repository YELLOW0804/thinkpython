import string

print string.punctuation
   
def process_line(line):
    line = line.replace('-', ' ')
    print line
    res = []
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        res.append(word)
    return res

line = 'A red pawn took a white pawn; this way. You see, Alice It\'s like a battle!'
l = process_line(line)
print l  
s = 'zhangchi!    '
print s.strip(string.punctuation + string.whitespace + 'zi'),s