def avoids(word, s):
    for letter in word:
        for l in s:
            if letter == l:
                return False
    return True

print avoids('yellow', 'wo')
line = raw_input('>')
fin = open('words.txt')
count = 0
num = 0
for l in fin:
    if avoids(l, line):
        count += 1
print count