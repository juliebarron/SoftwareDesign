from swampy.TurtleWorld import *
import math
from math import *

world = TurtleWorld()
bob = Turtle()
print bob

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

#square(bob, 100)

def polygon(t, n, length):
	for i in range(n):
		fd(t, length)
		lt(t, 360.0/n)

print polygon(bob, 7, 72)		

def circle(t, r):
	circumference = 2 * math.pi * r 
	n = int(circumference / 3) + 1
	length = circumference / n
	polygon(t, n, length)

bob.delay = 0.01

#circle(bob, 50)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * (angle/360.0)
	n = int(arc_length / 3) + 1 
	step_length = arc_length / float(n) 
	step_angle = float(angle) / float(n)
	for i in range(n):
		fd(t, step_length)
		lt(t, step_angle)

#arc(bob, 50, 180)

wait_for_user()

