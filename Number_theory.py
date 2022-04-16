from collections import defaultdict as d
from Primes import sieve_of_eratosthenes

'''
Q1: Find number of trailing zeros in a factorial

EXAMPLE: INPUT: 5! = 120 
		 OUTPUT: 1 	(120 has 1 trailing 0)

'''

def trailing_zeros(n):

	res = 0;
	while n>1:
		n//=5		
		res+=n
	return res

'''

Q2: Find the maximum power of a number in a factorial

EXAMPLE: INPUT: 25!, 8
		 OUTPUT: 7 (maximum power of 8 in 25! is 7)
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
'''

Q2: GCD of n numbers (without using math.gcd)

'''

def GCD(*n):
	numbers = d(int)
	for i in n:
		l = i
		prime_factors = d(int)
		for j in range(2, i+1):
			if j<=1:	break
			elif i%j == 0:
				while i%j == 0:
					prime_factors[j]+=1
					i//=j
		numbers[l] = prime_factors
	end = max(numbers[n[0]].items(), key = lambda i:i[0])
	all_primes = sieve_of_eratosthenes(end[0]+1)
	comm = {}
	for p in all_primes:
		for number, factors in numbers.items():
			if p in factors:
				if p not in comm:
					comm[p] = factors[p]
				else:
					comm[p] = min(comm[p], factors[p])
			else:
				comm[p] = 0
	prod = 1
	for fact, power in comm.items():
		if power:
			prod*=fact**power
	return prod


