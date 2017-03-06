def is_palindrome(s):
    return s[::-1] == s

for i in range(999999):
    if i > 100000:
        s = str(i)
        if (is_palindrome(s[2:]) and
        is_palindrome(str(i + 1)[1:]) and
        is_palindrome(str(i + 2)[1:5]) and
        is_palindrome(str(i + 3))):
            print i

