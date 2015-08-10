# -*- coding: utf-8 -*-
__author__ = 'XuJunjie'

import math
from pylab import *


def Binomial(n,i):
	return math.factorial(n)/(math.factorial(n-i)*(math.factorial(i)))

def BezierFunction(n):
	B = []
	for t in T:
		B_t = []
		for i in range(n+1):
			B_t.append(Binomial(n,i)*(t**i)*((1-t)**(n-i)))
		B.append(B_t)
	return mat(B)

def BezierCure(P):
	B_C = BezierFunction(shape(P)[0]-1)*P
	return B_C[:,0],B_C[:,1]

if __name__ == '__main__':
	T = np.linspace(0,1,100,endpoint = True)
	P = [[5,0],[6,5],[10,-5],[12,-2]]
	X,Y = BezierCure(mat(P))
	plot(X,Y)
	show()
