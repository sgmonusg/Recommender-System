import numpy
import random
import math
import svd

def calculate_frobenius(orig,result):
	#!returns the frobenius error given the original matrix and the newly constructed matrix
	[no_row,no_col]=orig.shape
	error=0;
	for i in range(0,no_row):
		for j in range(0,no_col):
			error+=(orig[i,j]-result[i,j])**2
	return math.sqrt(error)		
			
def choose_rand(probarr):
	#!return arandom columns or row depending on its probability
	sortarr=sorted(probarr.iteritems(),key=lambda (k,v):(v,k))
	index=[]
	prob=[]
	elements=0
	for i,val in sortarr:
		elements+=1
		index.append(i)
		prob.append(val)
	#print index
	#print prob	
	for i in range(1,elements):
		prob[i]=prob[i]+prob[i-1]
	x=random.random()
	#print prob
	i=0;
	#print x
	while(x>prob[i]):
		i+=1
	return index[i]

def CUR(A,srow,scol):
	#!calculating  the cur decomposition of given matrix a and the num of sampling rows and columns as srow,scol repectively
	#!it returns the frobenius error, reconstructed matrix and the three C , U , R matricies  
	# mXn= mXc  cXc  cXn
	#A=numpy.matrix('4,0,0,1;2,1,0,0;0,0,0,3')
	#print A[i,j]
	#print(A)
	no_col=4
	no_row=3
	no_row,no_col=A.shape
	no_sample_row=srow
	no_sample_column=scol
	Acalc=numpy.zeros(shape=(no_row,no_col))
	Cmatrix=numpy.zeros(shape=(no_row,no_sample_column))
	Rmatrix=numpy.zeros(shape=(no_sample_row,no_col))
	#Cmatrix[0,0]=1
	#print Cmatrix[0,0]
	PCOL={}
	PROW={}
	sampled_columns=[]
	sampled_rows=[]
	sum_square=0
	for t in A.getA1():
		sum_square+=(t**2)
	#print ("sum of square of elements is "+str(sum_square))
	#print A[0].getA1()[0]
	for i in range(0,no_col):
	  COL=	A.getT()[i].getA1()
	  #print i
	  #print COL
	  add=0
	  for x in COL:
		#print x
		add+=x**2
	  PCOL[i]= float(add)/sum_square
	#Make C
	for i in range(0,no_sample_column):
		j=choose_rand(PCOL)
		#print j
		sampled_columns.append(j)
		for k in range(0,no_row):
			Cmatrix[k,i]=float(A[k,j])/math.sqrt(no_sample_column*PCOL[j])
	for i in range(0,no_row):
		ROW=A[i].getA1()
		#print i
		#print ROW
		add=0
		for x in ROW:
			#print x
			add+=x**2
		PROW[i]= float(add)/sum_square
	#Make R
	for i in range(0,no_sample_row):
		j=choose_rand(PROW)
		sampled_rows.append(j)
		for k in range(0,no_col):
			Rmatrix[i,k]=A[j,k]/math.sqrt(no_sample_row*PROW[j])
	#print ("\nC matrix is :-\n")
	#print Cmatrix
	#print ("\nR matrix is:-\n")
	#print Rmatrix	

	#GET U

	#sampled_rows=sorted(sampled_rows)
	#sampled_columns=sorted(sampled_columns)
	Wmatrix=numpy.zeros(shape=[no_sample_row,no_sample_column])
	Umatrix=numpy.zeros(shape=[no_sample_row,no_sample_column])
	#print ("\nSampled Rows are:-\n")
	#print sampled_rows
	#print ("\nSampled Columns are:-\n")
	#print sampled_columns
	for i in range(0,no_sample_row):
		for j in range(0,no_sample_column):
			Wmatrix[i,j]=A[sampled_rows[i],sampled_columns[j]]
	#print "\nOriginal Matrix A is:-\n"
	#print A
	#print "\n W matrix is :-\n"
	#print Wmatrix
	Umatrix=numpy.linalg.pinv(Wmatrix)
	#print Umatrix
	Acalc=numpy.dot(Cmatrix,numpy.dot(Umatrix,Rmatrix))
	#print '\nFrobenius Error\n'
	ferror=calculate_frobenius(A,Acalc)
	return ferror,Acalc,Cmatrix,Umatrix,Rmatrix



'''
if __name__ == '__main__':
	random.seed(1234567);
	#A=numpy.matrix('4,0,0,1;2,1,0,0;0,0,0,3')
	A=numpy.random.random((10,10))
	A=numpy.asmatrix(A)
	sum=0
	for i in range(0,10):
		err,Acalc,Cmatrix,Umatrix,Rmatrix=CUR(A,3,3)
		print err
		sum+=err
	print 'Average Frobenius Error for matrix :'+str(float(sum)/10)	
'''