def total(int_list):
    sum = 0
    for l in int_list:
        sum += l
    return sum
l = []
for i in range(100):
    l.append(i + 1)

print total(l)