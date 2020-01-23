""" Program to calculate GCD of 2 numbers 

Implementation of Exercise 6.5
Book: Think Python 2nd Edition by Allen B. Downey
Edition: 2e
Link: https://greenteapress.com/wp/think-python-2e/
"""

def gcd(a, b):
	if b!= 0:
		# recursion with remainder
		return gcd(b,a%b)
	else:
		# if one number is 0 then return non-zero number
		# recusion ends here
		return a

print('Enter Numbers to find their gcd')
a = int(input('a: ')) # read input and type cast it to integer
b = int(input('b: '))
print('\nGCD: ',gcd(a, b),'\n')


"""
Author: Varun Aggarwal
Username: aggarw82
Github: https://github.com/Environmental-Informatics/building-more-complex-programs-with-python-aggarw82
"""