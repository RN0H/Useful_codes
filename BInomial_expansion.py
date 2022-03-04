
'''
INPUT = (2m+4)^4   format: (ax + b)^n
OUTPUT = 16m^4+128m^3+384m^2+512m+256
'''

def expand(expr):
    ex, po = expr.split('^')    #seperate the power from the expression

    print(ex, po)
    
    ex = ex[1:-1]   #eliminating brackets
    if 	 po == '0':   return '1'
    elif po == '1':   return ex
    
    x,y = getterms(ex, ex[0] == '-')

    '''
    get a, x, b and n from (ax + b)^n
    if a has no coefficient, take it as 1 else a
    '''

    a, x = x[:-1], x[-1]
    n, b = int(po), int(y)
 
    if a == '': a = 1 #no coefficient
    else: a = int(a)

    '''
    Now we have the terms and the power
    all we need to do is find the coefficients

    SUM nCr x^(n-r)y^r is the expansion
	find the complete coefficient and the power
    
    '''

    res = []
    for r in range(n+1):
    	power = n-r
    	totalcoef = int(coef(n, r)*a**(power)*b**(r))

    	term = ['', x, f"{x}^{power}"][min(power, 2)]

    	if totalcoef >=1:                      #positive
    		if totalcoef == 1 and power == n:     res.append( f"{term}")
    		elif totalcoef == 1 and power == 0:   res.append( f"{totalcoef}")
    		else:                                 res.append( f"+{totalcoef}{term}")
    						
    	else: res.append(f"{totalcoef}{term}") #negative
    		
    expansion = ''.join(res)
    if expansion[0] == '+': return expansion[1:]	#if the first coefficient is positive
    return expansion

def coef(n, r):
	'''
	nCr = n!/(n-r)!r!
	'''
	numerator, denominator= 1, 1
	for x in range(n, 0,-1):

		if x <= r: break
		else:
			numerator*=x
			denominator*=n-(x-1)
	
	return numerator/denominator
   
def getterms(ex, minus):
    if '+' in ex: x, y = ex[minus:].split('+')
    else:         x, y = ex[minus:].split('-'); y = '-'+y
    if minus: x = '-' + x
    return x,y
