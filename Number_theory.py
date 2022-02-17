from collections import defaultdict as d

'''
Q1: Find number of trailing zeros in a factorial

Example: INPUT: 5! = 120 
		 OUTPUT: 1 	(120 has 1 trailing 0)

'''

def trailing_zeros(n):

	res = 0;
	s = 5
	while s < n:
		res+= n//s
		s*=5
	return res

'''

Q2: Find the maximum power of a number in a factorial

EXAMPLE: 

'''

def maxpow(factorial, number):

	'''
	Create a hashtable of {primes:exponent}.

	Decompose the number into primes.

	'''
	prime_factors = d(int)
	for i in range(2, number+1):
		if number<=1:	break
		elif number%i == 0:
			while number%i == 0:
				prime_factors[i]+=1
				number//=i
	'''
	for every prime factor find its highest exponent
	in that factorial.

	Then divide the highest exponent by its exponent
	in the number.	
	'''
	for i in prime_factors:
		exp = 0
		f = factorial
		while f>=1:
			f//=i
			exp+=f
		prime_factors[i] = exp//prime_factors[i]

	'''
	Find the minimum exponent in the hashtable 
	which will be  the exponent of the number.
	'''
	power = prime_factors[min(prime_factors, key = lambda k: prime_factors[k])]
	
	return power
