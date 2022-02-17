from collections import defaultdict as d

'''

Q1: Find number of trailing zeros in a factorial

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
TBD
'''

def maxpow(factorial, n):

	'''
	Decompose n into primes
	'''
	c = d(int)
	
	for i in range(2,n+1):
		if n<=1:
			break
		elif n%i == 0:
			while n%i == 0:
				c[i]+=1
				n//=i
	for i in c:
		exp = 0
		f = factorial
		while f>=1:
			f//=i
			exp+=f
		c[i] = exp//c[i]
	power = c[min(c, key = lambda k: c[k])]
	return power

