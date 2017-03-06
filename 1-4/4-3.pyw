from swampy.TurtleWorld import *

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)
		
def draw_bob_square(bob, length):
	square(bob, length)
	
wordl = TurtleWorld()
bob = Turtle()

draw_bob_square(bob, 200)




