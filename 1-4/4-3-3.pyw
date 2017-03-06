from swampy.TurtleWorld import *

def square(t, length, n):
	for i in range(n):
		fd(t, length)
		lt(t, 360/n)
		
#def draw_bob_square(bob, length, n):
#	square(bob, length, n)
	
wordl = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
square(bob, 5, 360)
