from swampy.TurtleWorld import *

def koch(t, length):
    if length < 100:
        fd(t, length)
        return
    angle = 60
    koch(t, length / 3.0)
    lt(t, angle)
    koch(t, length / 3.0)
    rt(t, 180 - angle)
    koch(t, length / 3.0)
    lt(t, angle)
    koch(t, length / 3.0)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0

#for i in range(3):
#    koch(bob, 1000)
#    rt(bob, 120)

pu(bob)
rt(bob)
fd(bob, 200)
pd(bob)
lt(bob)

koch(bob, 1000)
die(bob)

world.canvas.dump()

wait_for_user()
