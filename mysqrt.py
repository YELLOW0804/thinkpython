import math
def nSqrt(x):
    a = 3.0
    count = 0
    while True:
        count = count + 1
        y = (a + x / a) / 2
        if abs(y - a) < 0.00000001:
            break
        a = y
    return y


def test_square_root():
    i = 1.0
    while i <= 10:
        print i, nSqrt(i), math.sqrt(i), abs(nSqrt(i) - math.sqrt(i))
        i = i + 1

test_square_root()