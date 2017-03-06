def is_power(a, b):
    if b == 0:
        return False
    if a == b or b == 1:
        return True
    if a % b == 0:
        return is_power(a / b, b)
    return False

print is_power(8, 6)