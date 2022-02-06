'''
PROBLEM STATEMENT: In how many ways can the letters of the word ${WORD} be 
				   rearranged such that the vowels always appear together?

EXAMPLE: 	Input: WORD = ACCLAIM
			Output: 180
'''


from math import factorial as fact
from collections import defaultdict as d

VOWELs ={'A':0, 'E':0, 'I':0, 'O':0, 'U':0}

def ways(word):
	'''
	Initializing: number of non-vowels <- 0
				  number of vowels     <- 0
				  hash table of non vowel
	'''
	word_count, vowel_count,  WORDs = 0, 0, d(int)

	'''
	Find the vowels & non-vowels,
	Count the number of vowels and non-vowels

	'''

	for letter in word:

		if letter.upper() in VOWELs:
			VOWELs[letter]+=1
			vowel_count+=1
		else:
			WORDs[letter]+=1
			word_count+=1

	'''
	Find the number of ways to arrange the vowels
	'''
    
	denominator = 1
	for vowel, number in VOWELs.items():
		if number>1:
			denominator*=fact(number)

	vowel_perm = fact(vowel_count)/denominator

	'''
	Find the number of ways to arrange the non-vowels
	'''
	denominator = 1
	for word, number in WORDs.items():
		if number>1:
			denominator*=fact(number)

	words_perm = fact(word_count)/denominator

	'''
	The vowels are together, therefore there are 'non-vowels+1' spaces
	'''

	return int(vowel_perm*words_perm*(word_count + 1))

print(ways('ACCLAIM'))