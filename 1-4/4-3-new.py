from swampy.TurtleWorld import *
import math
def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)
def polyline(t, length, n, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, length, n, angle)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, step_length, n, step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)
    

def flower(t, r, angle, n):
    step_angle = 360.0 / n;
    for i in range(n):
        petal(t, r, angle)
        lt(t, step_angle)

def diagonalLow2(t, r, n):
    angle_top = 360.0 / n
    angle_bottom = (180 - angle_top) / 2
    r = length / (2 * math.cos(angle_bottom))
    print int(r)
    
def draw_spiral(t, n, length=3, a=0.1, b=0.0005):
    theta = 0.0

    for i in range(n):
        fd(t, length)
        dtheta = 1 / (a + b * theta)

        lt(t, dtheta)
        theta += dtheta
    

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.005
draw_spiral(bob, 100)

wait_for_user()
