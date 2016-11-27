import CUR	
import numpy as np
import svd
import time
import random

if __name__ == "__main__":
	x=10
	for i in range(1,51):
		# creating the file for writing the SVD and CUR matricies
		svdfile = open('svd_'+str(i)+'.txt', 'w')
		curfile = open('cur_'+str(i)+'.txt', 'w')
		matrix=np.random.random((x,x))
		t=time.clock()
		#function call to do a single value decomosition on  matrix m
		u ,v, sigma =svd.SVD_Matrix_show(matrix)
		# function call to make the new matrix after SVD
		new_matrix=svd.remakeSVD(u , v, sigma)
		print x
		print 'for SVD time:'+str(time.clock()-t)
		print >>svdfile, u,v,sigma		
		t=time.clock()
		# getting the martix from the CUR Fuction 
		err,Acalc,Cmatrix,Umatrix,Rmatrix=CUR.CUR(np.asmatrix(matrix),int(x/2),int(x/2))
		print '\nfor CUR time:'+str(time.clock()-t)
		print >>curfile, Cmatrix,Umatrix,Rmatrix
		#closing the file operation 
		svdfile.close()
		curfile.close()
		x+=20
		print '\n\n'