def is_between(x, y, z):
    if x <= y and y <= z and x <= z:
        return True
    else:
        return False
def is_between_low(x, y, z):
    if x <= y and y <= z: #and x <= z:
        return True
    else:
        return False

print is_between(1, 2, 3)
print is_between(9, 21 , 10)

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if is_between(i, j, k) != is_between_low(i, j, k):
                print True, i, j, k
