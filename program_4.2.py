""" Program to draw flowers

Implementation of Exercise 4.2
Book: Think Python 2nd Edition by Allen B. Downey
Edition: 2e
Link: https://greenteapress.com/wp/think-python-2e/
"""

import turtle
import math

def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def flower(n, r, a, t):
	""" Draw flower with n petals 
	n: number of petals
	a: angle turtle moves before turning 
	r: radius of petal
	"""
	i = 0
	while i != n:

		# loop to draw petal
		j = 1
		while j != 3:
			arc(t, r, a)
			t.lt(180 - a) # turn turtle for second half of petal
			j += 1

		# turn tutle for next petal
		t.lt(360.0/n)
		i += 1 # outer loop counter

whatsupdoc = turtle.Turtle()
whatsupdoc.speed('fastest')


""" flower 1 """

# move to new spot
whatsupdoc.pu()
whatsupdoc.fd(-200)
whatsupdoc.pd()
#start drawing
flower(7, 100, 60, whatsupdoc)



""" flower 2 """

# move to new spot
whatsupdoc.pu()
whatsupdoc.fd(200)
whatsupdoc.pd()
#start drawing
flower(10, 80, 80, whatsupdoc)


""" flower 3 """

# move to new spot
whatsupdoc.pu()
whatsupdoc.fd(200)
whatsupdoc.pd()
#start drawing
flower(20, 260, 20, whatsupdoc)
turtle.mainloop()


"""
Author: Varun Aggarwal
Username: aggarw82
Github: https://github.com/Environmental-Informatics/building-more-complex-programs-with-python-aggarw82
"""