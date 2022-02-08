

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

