import math
def eval_loop():
    while True:
        line = raw_input('>')
        if line == 'done':
            print lastLine + ' L'
            break
        lastLine = line
        print eval(line)

eval_loop()