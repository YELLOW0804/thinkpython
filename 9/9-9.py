def is_palindrome(s, n):
    return s[::-1] == n

count = 0
dt = 9
my_age = 0
cur_age = 0

while dt < 50:
    while my_age < 99:
        mon_age = my_age + dt
        if is_palindrome(str(my_age).zfill(2), str(mon_age).zfill(2)):
            count += 1
            print str(my_age) + ' ' + str(mon_age) + ' ' + str(dt) + ' ' + str(count)
        my_age += 1

    my_age = 0
    count = 0
    dt += 1


         