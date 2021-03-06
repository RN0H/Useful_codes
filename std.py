import numpy as np
import matplotlib.pyplot as plt
from quartile import Median


def std(data, stepsize):
	'''
	mean(μ) = (Σ data)/(length of data)

	variance = (Σ(x - mean)(x-mean).T)/(length of data)

	standard deviation(σ) = (variance)^1/2

	'''
	data.sort()
	mean = sum(data)/len(data)
	mode = max(data, key = lambda i: data.count(i))

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
	constant = 1#0.39894228062936171/std

	
	median = Median(data)

	likelihood = lambda i: constant*np.exp(-((i-mean)**2)/2*var)

	plt.grid()

	plt.plot(spread, constant*np.exp(-((spread - mean)**2)/2*var), 'r', \
			[mean for _ in np.arange(0,likelihood(mean),stepsize)], np.arange(0,likelihood(mean),stepsize), 'b', \
			[median for _ in np.arange(0,likelihood(median),stepsize)], np.arange(0,likelihood(median),stepsize), 'g', \
			)
	plt.plot([mode for _ in np.arange(0,likelihood(mode),stepsize)], np.arange(0,likelihood(mode),stepsize), 'purple', linestyle = "dashdot")
	plt.legend(['Normal distribution', 'mean', 'median', 'mode'], loc = 'upper right')
	plt.xlabel("Dataset"); plt.ylabel("likelihood")
	print("Mean={}\nMode={}\nMedian={}\nSTD={}".format(mean,mode,median,std))

	plt.show()




print(std([1,2,3,4], 0.0001))