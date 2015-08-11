# -*- coding: utf-8 -*-
__author__ = 'XuJunjie'

import math
from pylab import *#pylab.pinv
from scipy.misc import comb

def BezierFunction(n):
	B = [[comb(n,i)*(t**i)*((1-t)**(n-i)) for i in range(n+1)] for t in T]
	return mat(B)

def BezierCure(P):
	B_C = BezierFunction(shape(P)[0]-1)*P
	return B_C[:,0],B_C[:,1]



if __name__ == '__main__':
	T = np.linspace(0,1,100,endpoint = True)
	P = [[5,0],[6,5],[10,-5],[12,-2],[11,0]]
	X,Y = BezierCure(mat(P))
	plot(X,Y)
	show()
