""" Program which allows users to Challenge Fermat's Last Theorem

Implementation of Exercise 5.2 Part 2
Book: Think Python 2nd Edition by Allen B. Downey
Edition: 2e
Link: https://greenteapress.com/wp/think-python-2e/
"""

def check_fermat(a,b,c,n):

	# compound if condition with &
	if (a**n + b**n == c**n) & n > 2:
		print('\n\nHoly smokes, Fermant was wrong\n')
	else:
		print('\nNo, that doesn\'t work\n')

def user_inputs():
	print('Enter Values for equation: a^n + b^n = c^n')
	print('Only Integers are permitted')
	a = int(input('Value of a: ')) # read input and type cast it to integer
	b = int(input('Value of b: '))
	c = int(input('Value of c: '))
	n = int(input('Value of n: '))
	check_fermat(a,b,c,n) 

user_inputs()


"""
Author: Varun Aggarwal
Username: aggarw82
Github: https://github.com/Environmental-Informatics/building-more-complex-programs-with-python-aggarw82
"""