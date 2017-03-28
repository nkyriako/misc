import numpy as np
import timeit
import matplotlib.pyplot as plt
import math
def matmult(A,x):
    n=len(x)
    B=[]
    for i in range(n):
        Sum=0
        for j in range(n):
            Sum+=A[i][j]*x[j]#makes an array with i rows and j columns 
        B.append(Sum)
    return np.array(B)
#########################################################################
def hadmat(k):#T(2^k)
    if k==1:
        return np.array([[1,1],[1,-1]]) #O(1)
    had=[]
    subhad=hadmat(k-1)
    n2=len(hadmat(k-1))
    for i in range(n2):
        had.append(np.concatenate([subhad[i],subhad[i]]))
    for j in range(n2):
        had.append(np.concatenate([subhad[j],-subhad[j]]))
    return np.array(had)
    #T(n)=c*n^2 /4 = O(n^2) 
#########################################################################
def hadmatmult(H,x):#T(n)
    n=len(x)#O(1)
    if n==2:#O(n^2) for small size (n=2), so effectively O(1)
        return matmult(hadmat(n-1),x)
    Lmult=hadmatmult(hadmat(math.log(n/2,2)),np.split(x,2)[0])#T(n/2)
    Rmult=hadmatmult(hadmat(math.log(n/2,2)),np.split(x,2)[1])#T(n/2)
    TopAdd=[]
    BotAdd=[]
    for i in range(n//2):#O(n/2 * 2)=O(n)
        TopAdd.append(Lmult[i]+Rmult[i])
        BotAdd.append(Lmult[i]-Rmult[i])
    return np.array(TopAdd+BotAdd)
    #T(n)=2T(n/2)+O(n) - > T(n) = O(nlogn)
##########################################################################
def fnk(x,k):
	n=len(x)
	if n==2 and k==0:
		return x[0]+x[1]
	if n==2 and k==1:
		return x[0]-x[1]
	if k<int(n/2):
		return fnk(np.split(x,2)[0],k)+fnk(np.split(x,2)[1],k)#recursion onto x[0] and x[1]
	if k>=int(n/2):
		return fnk(np.split(x,2)[0],k%(int(n/2)))-fnk(np.split(x,2)[1],k%(int(n/2)))
def efficienthadmatmult(x):
	C=[]
	for k in range(len(x)):
		C.append(fnk(x,k))
	return np.array(C)
###########################################################################
#graph size vs runtime
# timing=[]
# timing2=[]
# for i in range(1,13):
#     A=hadmat(i)
#     B=np.random.random_integers(1,2**i,2**i)
#     start=timeit.default_timer()
#     hadmatmult(A,B)
#     stop=timeit.default_timer()
#     timing.append(stop-start)
#     start=timeit.default_timer()
#     matmult(A,B)
#     stop=timeit.default_timer()
#     timing2.append(stop-start)
# line1=plt.plot([x for x in range(1,13)],timing,label='hadmatmult runtime')
# line2=plt.plot([x for x in range(1,13)],timing2,label='matmult runtime')
# plt.title('n  vs time')
# plt.xlabel('n') 
# plt.ylabel('time')
# plt.legend()
# plt.show()