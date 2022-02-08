

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

Q2: Find power of a non-prime in a factorial
TBD
'''

