

def prime(n):
	primes = []
	for i in range(2, n+1):
		if is_prime(i):
			primes.append(i)
	return primes


def is_prime(i):
	for j in range(2, int(i**.5)+1):
			if i%j == 0:
				return False
	return True


sum_of_all_primes = lambda n: sum(i for i in range(2,n+1) if is_prime(i))
is_prime = lambda i: all(i%j for j in range(2,int(i**.5)+1))

print(prime(20))