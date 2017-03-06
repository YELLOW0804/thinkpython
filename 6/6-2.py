import math

def hypotenuse(a, b):
    power_a = a ** 2
    print power_a
    power_b = b ** 2
    print power_b
    power_c = power_a + power_b
    print power_c
    c = math.sqrt(power_c)
    print c
    return c

hypotenuse(1, 1)
