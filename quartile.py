

'''
A spread of data can be divided into 4 parts called as "quartiles"

'''


def quartile(x):
	if len(x)<4: return 'Enter at least 4 data points!'
	'''
	data should be sorted
	'''
	x = sorted(x)

	'''
	return [Q1, Q2, Q3] ..WHERE Q is quartile
	'''
	return [Median(x[:len(x)>>1]), Median(x), Median(x[(len(x)&1)+len(x)>>1 :])]

def Median(x):
	length = len(x)
	half = length>>1
	
	'''
	if length is odd -> select the middle
	else -> select 2 middle elements and find their average
	'''

	middle = x[half -(~length&1) : half + 1]
	median = sum(middle)/len(middle)
	return median

