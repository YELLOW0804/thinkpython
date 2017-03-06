def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))
know = {}
def ackermann(m, n):
    if (m, n) in know:
        return know[m, n]
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    know[m, n] = ackermann(m - 1, ackermann(m, n - 1))
    return know[m, n]



print ack(3, 4)
print ackermann(3, 4)
print know
