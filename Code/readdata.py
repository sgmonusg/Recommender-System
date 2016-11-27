import sys
import os
import numpy as np

file_handler=open("ratings.txt",'r')
fil=file_handler.read()
file_handler.close()
lines=fil.splitlines()
s=(1508,2071)
mat=np.zeros(s)
print mat
temp=0

for x in lines:
	data=x.split()
	x=int(data[0])
	y=int(data[1])
	rat=float(data[2])
	#print rat
	mat[x-1,y-1]=rat
	#print mat[x-1,y-1]
	#//entry=data.split()
	#print data
	#print data[0]
	#y=int(data[1])
	#if y>temp:
	#	temp=y
	#print temp
	#print data[2]
		
f=open("config_mat.txt","w")
f.write(mat)
f.close()


