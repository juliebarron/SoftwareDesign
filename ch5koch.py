from swampy.TurtleWorld import *
import math
from math import *

world = TurtleWorld()
t = Turtle()
print t

def draw_kochcurve(t, x):
	if x < 3:
		fd(t, x)
	else:
		draw_kochcurve(t, x/3)
		lt(t, 60)
		draw_kochcurve(t, x/3)
		rt(t, 120)
		draw_kochcurve(t, x/3)
		lt(t, 60)
		draw_kochcurve(t, x/3)
		
t.delay = 0.01

draw_kochcurve(t, 200)

wait_for_user()
