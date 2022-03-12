import timeit 

def prime(m, n)->list:
	primes = []
	if m == 1: m+=1
	for i in range(m, n+1):						#Iterating from 2 -> n+1
		if is_prime(i):							#call back
			primes.append(i)					#add to list if true else no
	return primes


def is_prime(i)->bool:
	for j in range(2, int(i**.5)+1):			#Since we can iterate all the way to 'i', why waste time instead to i^0.5
			if i%j == 0:						#if divisible, then 'i' is not prime
				return False 					
	return True



#prime = lambda n: [i for i in range(2,n+1) if is_prime(i)]		#code golf variation
#is_prime = lambda i: all(i%j for j in range(2,int(i**.5)+1))	#code golf variation


def sieve_of_eratosthenes(n):
	'''
	Create a boolean array of length n
	This is important to check the validity
	if the index of the array based on the truth value

	'''
	table = [1 for _ in range(n+1)]
	'''
	The smallest prime number is 2.
	Therefore all the numbers from 2^2 = 4
	till n at steps of 2 will all be non-prime.
	We need to mark these numbers as False

	After than we move onto 3..

	Numbers from r^2 till n are marked as false 
	by taking intervals of r steps. If r is already
	marked as false then we can ignore it. 
	'''

	s,ssq = 2, 4
	while (ssq<=n):

		if table[s] == 1:
			for _ in range(ssq, n+1, s):
				table[_] = 0
		s+=1
		ssq = s*s
	return [i for i in range(2, n+1) if table[i]]

a = 1000000

start = timeit.default_timer()
v = sieve_of_eratosthenes(a)
print("Exectution time: {}ms".format(1e3*(timeit.default_timer()-start)))

start = timeit.default_timer()
assert v == prime(2,a)
print("Exectution time: {}ms".format(1e3*(timeit.default_timer()-start)))

