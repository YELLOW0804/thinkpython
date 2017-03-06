know = {0:0, 1:1}

import time
def fibonacci(n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'factorial is only define for negative integers.'
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_ex(n):
    if n in know:
        return know[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    know[n] = res
    return res
start = time.time()
f = fibonacci_ex(30)
end = time.time() - start
print end,f
start = time.time()
f = fibonacci(30)
end = time.time() - start
print end,f