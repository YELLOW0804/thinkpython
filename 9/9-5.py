def uses_all(word, letters):
    for line in letters:
        if not (line in word):
            return False
    return True

#print uses_all('yellow', 'yel')

fin = open('9\words.txt')
count = 0
for line in fin:
    if uses_all(line, 'aeiouy'):
        count += 1
        if count < 10:
            print line

print count