def is_triangle(a, b, c):
    if a + b >=c and b + c >= a and a + c >= b:
        print 'Yes'
    else :
        print 'No'

def check_triangle():
    a = int(raw_input('Input a triangle edge:\n'))
    b = int(raw_input('Input a triangle edge:\n'))
    c = int(raw_input('Input a triangle edge:\n'))

    is_triangle(a, b, c)

check_triangle()
