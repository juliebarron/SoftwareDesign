from swampy.TurtleWorld import *
import math
from math import *

world = TurtleWorld()
t = Turtle()
print t
t.delay = 0.01

def dragon_start(t, d, n):
	if n == 0:
		return
	fd(t, d)
	dragon_x(t, d, n)

def dragon_x(t, d, n):
	if n == 0:
		return
	dragon_x(t, d, n-1)
	rt(t)
	dragon_y(t, d, n-1)
	fd(t, d)

def dragon_y(t, d, n):
	if n == 0:
		return
	fd(t, d)
	dragon_x(t, d, n-1)
	lt(t)
	dragon_y(t, d, n-1)

dragon_start(t, 20, 10)

wait_for_user()
