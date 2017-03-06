def factorial(n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'factorial is only define for negative integers.'
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(100):
    print factorial(i)
