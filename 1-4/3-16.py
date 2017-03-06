def do_twice(f, str):
	f(str)
	f(str)

def print_yellow(str):
	print str
	
do_twice(print_yellow, 'yellow')

def do_four(f, str):
	do_twice(f, str)
	do_twice(f, str)
	
do_four(print_yellow, 'blue')