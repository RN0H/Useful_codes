from collections import defaultdict as d

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

Q2: last digit of (x^(x1^(x2....)))

'''

table = {0:(1, {0:0}),
		1:(1, {0:1}),					#{digit: (mod, map)}
		2:(4, {1:2, 2: 4, 3:8, 0:6}), 
		3:(4, {1:3, 2:9, 3:7, 0:1}), 
		4:(2, {1:4, 0:6}), 
		5:(1, {0:5}),
		6:(1, {0:6}),
		7:(4, {1:7, 2:9, 3:3, 0:1}),
		8:(4, {1:8, 2:4, 3:2, 0:6}),
		9:(2, {1:9, 0:1})}
def last_digit(lst):
    if len(lst)<=1 or lst == [0, 0]: return 1
    print(lst)
    while len(lst)>2:
        mod, d = table[int(str(lst[-2])[-1])]
        if lst[-1] == 0:
            lst[-2] = 1
        elif lst[-1] == 1:
            pass
        else:
            a = d[lst[-1]%mod]
            lst[-2]*=a
        lst.pop()
    mod, d = table[int(str(lst[-2])[-1])]
    a = d[lst[-1]%mod]
    return a