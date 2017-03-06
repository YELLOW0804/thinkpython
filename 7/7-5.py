import math
def estimate_pi():
    k = 0
    c = 2 * math.sqrt(2) / 9801
    backpi = 0
    while True:
        up = math.factorial(4 * k) * (1103 + 26390 * k)
        down = ((math.factorial(k)) ** 4) * (396 ** (4 * k))
        i = c *  up / down
        backpi += i
        if abs(i) < 1e-15:
            break
        k += 1
        print k
    return 1 / backpi

print estimate_pi()

        
