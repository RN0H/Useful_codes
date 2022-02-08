import numpy as np
import matplotlib.pyplot as plt


def std(data, stepsize):
	'''
	mean(μ) = (Σ data)/(length of data)

	variance = (Σ(x - mean)(x-mean).T)/(length of data)

	standard deviation(σ) = (variance)^1/2

	'''
	data.sort()
	mean = sum(data)/len(data)

	var = sum((i - mean)**2 for i in data)/len(data)

	std = var**.5
	'''
	quality of the distribution using the step-size

	'''

	spread = np.arange(data[0], data[-1], stepsize)

	'''
	plot 
	F(μ, σ, x) = (1/σ√2π)e^((−(x−μ)(x−μ).T)/2σ^2)
	constant = (1/σ√2π)
	'''
	constant = 0.39894228062936171/std


	plt.grid()

	plt.plot(spread, constant*np.exp(-((spread - mean)**2)/2*var), 'r', \
			[mean for _ in np.arange(0,constant,stepsize)], np.arange(0,constant,stepsize), 'b')
	plt.legend(['Normal distribution', 'μ'], loc = 'upper right')

	plt.show()

