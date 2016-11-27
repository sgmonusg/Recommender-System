import CUR
import svd
import numpy as np
import random

if __name__ == "__main__":
	# a random seed is used to generate a fixed random array for all test cases
	random.seed(123456)
	# x is the dimension of the matrix the test matricies are of the form x*x
	x=10000000
	print x
	matrix=np.random.random((x,x))
	#function call to do a single value decomosition on  matrix m
	u ,v, sigma =svd.SVD_Matrix_show(matrix)
	# function call to make the new matrix after SVD
	new_matrix=svd.remakeSVD(u , v, sigma)
	# calculate the frobenius error for SVD
	error=svd.calculate_frobenius(matrix , new_matrix)
	print '\nFrobenius Error for SVD:'
	print error
	# coverting a numpy nd array into a numpy matrix
	matrix=np.asmatrix(matrix)
	# calculating the frobenius error for CUR
	err,Acalc,Cmatrix,Umatrix,Rmatrix=CUR.CUR(matrix,int(x/2),int(x/2))
	print '\nFrobenius Error for CUR:'
	print err
