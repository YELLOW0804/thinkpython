from swampy.TurtleWorld import *
import math

def polyline(t, n, length, angle):
        """draw n line segments with the given length and
        angle(in degrees) between them. t is a turtle.
        """
        for i in range(n):
                fd(t, length)
                lt(t, angle)

def polygon2(t, n, length):
        angle = 360.0 / n
        polyline(t, n, length, angle)

def arc2(t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = float(angle) / n
        polyline(t, n, step_length, step_angle)

def circle2(t, r):
        arc2(t, r, 360)

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.

    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        fd(t, length)
        dtheta = 1 / (a + b * theta)

        lt(t, dtheta)
        theta += dtheta

def petal(t, r, angle):
        """Draws a petal using to arcs
        """
        for i in range(2):
                arc2(t, r, angle);
                lt(t, 180 - angle)
                
def flower(t, n, r, angle):
        """Draws a flower with n perals.
        """
        for i in range(n):
                petal(t, r, angle)
                lt(bob, 360.0/n)
        
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
flower(bob, 10, 50, 90)
