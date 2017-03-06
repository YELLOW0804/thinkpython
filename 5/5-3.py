import math

def check_fermat(a, b, c, n):
    left = math.pow(a, n) + math.pow(b, n)
    right = math.pow(c, n)
    if left == right :
        print 'Fermat is wrong!'
        print a, b, c, n
    else :
        print 'no!'

#check_fermat(3, 4, 5, 2)


#inputA = raw_input('Input a\n')
#inputB = raw_input('Input b\n')
#inputC = raw_input('Input c\n')
#inputN = raw_input('Input n\n')
#a = int(inputA)
#b = int(inputB)
#c = int(inputC)
#n = int(inputN)

#check_fermat(a, b, c, n)


for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(3, 10):
                check_fermat(i, j, k, l)


    

