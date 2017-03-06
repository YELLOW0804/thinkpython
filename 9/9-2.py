def has_no_e(word):
    for i in range(len(word)):
        if word[i] == 'e':
            return False
    return True

fin = open('9\words.txt')
count = 0
num = 0
for line in fin:
    if has_no_e(line.strip()):
#        print line.strip()
        count += 1
    num += 1

p = count * 1.0 / num
print count, num, p