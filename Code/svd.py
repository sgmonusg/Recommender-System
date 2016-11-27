import numpy as np
from numpy import linalg as LA
import math
import sys
import os
import random

def calculate_frobenius(orig,result):
	#!returns the frobenius error given the original matrix and the newly constructed matrix
	[no_row,no_col]=orig.shape
	error=0;
	for i in range(0,no_row):
		for j in range(0,no_col):
			error+=(orig[i,j]-result[i,j])**2
	return math.sqrt(error)	

def uSVD(a):
	#!function is used to compute the U Martix of the SVD given the original matrix a 
	#take transpose of matrix 
	b=np.matrix.transpose(a)
	initial= np.dot(a,b)
	# finding the egin values and vectors 
	# the numpy ndarray (v) is a column eigen vector which is orthonormalized
	w, v = LA.eig(initial)
	'''complex_check= np.iscomplex(v)
	k=0
	for x in complex_check:
		if x==True:
			#delete col frm w
			w=w.delete()
			k=k+1
		else:
			k=k+1'''
	return w,v

def v_transposeSVD(a):
	#!function is used to compute the V^T Martix of the SVD given the original matrix a
	# the above code is repeated for v matrix and the difference is the multiplication of A^T*A instead of A*A^T
	b=np.matrix.transpose(a)
	initial= np.dot(b,a)
	w ,v =LA.eig(initial)
	#the transpose of matrix v is taken for finding V^T matrix
	v_transpose=np.matrix.transpose(v)
	return v_transpose

def sigmaSVD(a , row , col):
	#!the function takes the num of rows and col and th elements of diagonal matrix as input and returns the diagonal matrix d
	d=np.eye(row,col)
	# creatation of diagonal identity matrix of size rowxcol
	k=0
	#print a
	a=np.sort(a)
	#sorting a numpy array in increasing order
	a= a[::-1]
	#used to reverse the array
	#print a (debugging)
	for i in a:
		d[k,k]=i
		k+=1
	return d

def remakeSVD(u , v, sigma):
	#!the function takes U ,V , Sigma as inputs and reforms the matrix after dimension reduction using svd and retruns the newly formed matrix
	remake=np.dot(u,sigma)
	remake=np.dot(remake,v)
	return remake

def SVD_Matrix_show(a):
	#!the main function for creating the whole process
	w, u = uSVD(a)
	#print w (debugging)
	#print(u) (debugging)
	v=v_transposeSVD(a)
	#print(v) (debugging)
	m,n=u.shape
	x,y=v.shape
	sigma=sigmaSVD(w,n,x)
	#print(sigma) (debugging)
	return u , v, sigma 


'''
if __name__ == "__main__":
	random.seed(1234567)
	matrix=np.random.random((10,10))
	u ,v, sigma =SVD_Matrix_show(matrix)
	new_matrix=remakeSVD(u , v, sigma)
	error=calculate_frobenius(matrix , new_matrix)
	print error
'''