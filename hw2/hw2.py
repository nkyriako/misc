import numpy as np
###################################################
def selectionsort(A):
	n=len(A)					#n is length of array
	i=0
	for i in range(n):			#carried out n times
		minindex=i
		for j in range(i+1,n):	
			if A[j]<A[minindex]: #find min in subarray of unsorted 
				minindex=j		
		temp = A[i]
		A[i]=A[minindex]		#switch min 
		A[minindex]=temp
	return A
###################################################
def insertionsort(A):
	n=len(A)
	for i in range(1,n):		#carried out n times
		j=i
		while j>0 and A[j-1]>A[j]:# finding the next smallest in list 
			temp=A[j-1]
			A[j-1]=A[j]		#switch with adjacent
			A[j]=temp
			j=j-1 				#move to next element 
	return A
###################################################
def mergesort(A):
	n=len(A)
	if n<=1:							#base case 
		return A
	B=np.array(A)
	L=np.array_split(B,2)[0] 			# split up and assign both halves of (sub)array 
	R=np.array_split(B,2)[1]
	Lsort=mergesort(L)					#recursion on left side
	Rsort=mergesort(R)					#recursion on right side 
	return merge(Lsort, Rsort)			#combine left and right 

def merge(Lsort, Rsort):
	Arr=[]
	i=0
	j=0
	Lsort=np.append(Lsort,1000000000) #this element is never actually used, its just a placeholder so 
	Rsort=np.append(Rsort,1000000000) #array doesn't go out of bounds.
	a=Lsort.size
	b=Rsort.size
	while i<a-1 or j<b-1:
		if Lsort[i]>Rsort[j]:			#compare first element in each subarray half 
			Arr.append(Rsort[j])		#if left is larger 
			j+=1
		elif Lsort[i]<=Rsort[j]:		#if right is equal to or larger 
			Arr.append(Lsort[i])
			i+=1
	return Arr