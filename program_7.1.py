""" Program to generate a table of comparison for
    own sqrt function vs math.sqrt() 

Implementation of Exercise 7.1
Book: Think Python 2nd Edition by Allen B. Downey
Edition: 2e
Link: https://greenteapress.com/wp/think-python-2e/
"""

import math

def mysqrt(a):
	x = a - 0.9 # initial guess for x

	# calculate square root until estimate stops updating
	while True:
		y = (x + a/x) / 2
		if y == x:
			break	
		x = y
	return x

def test_square_root():
	a = 1

	# format output
	print('\n\na     mysqrt(a)     math.sqrt(a)     diff')
	print('-     ---------     ------------     ----')
	
	# calculate and print for a = 1 to 9
	while a != 10:
		second_col = mysqrt(a)
		third_col = math.sqrt(a)
		diff = abs(third_col - second_col)
		print('{0:.1f}   {1:.5f}       {2:.5f}          {3}'.format(a,second_col,third_col,diff))
		a += 1
	print('\n')

test_square_root()


"""
Author: Varun Aggarwal
Username: aggarw82
Github: https://github.com/Environmental-Informatics/building-more-complex-programs-with-python-aggarw82
"""

