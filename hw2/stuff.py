'''
stuff.py
This is the script we used , one pdf at a time, to plot the graphs. 
'''

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import timeit
from hw2 import insertionsort, selectionsort, mergesort
import numpy as np


# ssort=[]
# msortforwards=[]
# msortbackwards=[]
# msort=[]
# for n in range(100,10300,300):
#         s=np.array([n-x for x in range(n)])
#         start=timeit.default_timer()
#         selectionsort(s)
#         stop=timeit.default_timer()
#         ssort.append(stop-start)

# for n in range(100,10300,300):
#         s=np.array([x+1 for x in range(n)])
#         start=timeit.default_timer()
#         selectionsort(s)
#         stop=timeit.default_timer()
#         msortforwards.append(stop-start)
#         s=np.array([n-x for x in range(n)])
#         start=timeit.default_timer()
#         selectionsort(s)
#         stop=timeit.default_timer()
#         msortbackwards.append(stop-start)		
# # for n in range(100,10300,300):
# #         s=np.array([n-x for x in range(n)])
# #         start=timeit.default_timer()
# #         mergesort(s)
# #         stop=timeit.default_timer()
# #         msort.append(stop-start)

# # plt.plot([x for x in range(100,10300,300)],ssort)
# plt.plot([x for x in range(100,10300,300)], msortforwards)
# plt.plot([x for x in range(100,10300,300)], msortbackwards)
# # plt.plot([x for x in range(100,10300,300)],msort)

# plt.ylabel('Runtime')
# plt.xlabel('Length of array')
# plt.title('Selection Sort on a Sorted/Unsorted Array')
# plt.show()

'''
u=np.array(np.random.random_integers(0,10**6,10**6))
print('10:20')
start=timeit.default_timer()
insertionsort(u)
stop=timeit.default_timer()
print(stop-start)
'''
'''
#Selection, Compare sorted to unsorted

ssort =[]
sunsort=[]
for n in range(100,10300,300):
        s=np.array([x+1 for x in range(n)])
        start=timeit.default_timer()
        selectionsort(s)
        stop=timeit.default_timer()
        ssort.append(stop-start)
for n in range(100,10300,300):
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        selectionsort(u)
        stop=timeit.default_timer()
        sunsort.append(stop-start)

plt.plot([x for x in range(100,10300,300)],ssort)
plt.plot([x for x in range(100,10300,300)],sunsort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Selection Sort: Sorted vs Reverse Sorted Input')
plt.show()
'''
'''
#merge.pdf
msort =[]
munsort=[]
for n in range(100,10300,300):
        s=np.array([x+1 for x in range(n)])
        start=timeit.default_timer()
        mergesort(s)
        stop=timeit.default_timer()
        msort.append(stop-start)
for n in range(100,10300,300):
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        mergesort(u)
        stop=timeit.default_timer()
        munsort.append(stop-start)

plt.plot([x for x in range(100,10300,300)],msort)
plt.plot([x for x in range(100,10300,300)],munsort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Merge Sort: Sorted vs Reverse Sorted Input')
plt.show()
'''
'''
#insert.pdf
isort =[]
iunsort=[]
for n in range(100,10300,300):
        s=np.array([x+1 for x in range(n)])
        start=timeit.default_timer()
        insertionsort(s)
        stop=timeit.default_timer()
        isort.append(stop-start)
for n in range(100,10300,300):
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        insertionsort(u)
        stop=timeit.default_timer()
        iunsort.append(stop-start)

plt.plot([x for x in range(100,10300,300)],isort)
plt.plot([x for x in range(100,10300,300)],iunsort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Insertion Sort: Sorted vs Reverse Sorted Input')
plt.show()
'''

#Randomized Average Runtime, All
mtimes=[]		
stimes=[]		
itimes=[]	
for n in range(100,10300,300):
        u=np.array(np.random.random_integers(0,n,n))
        t=0
        for _ in range(100):
                np.random.permutation(u)
                start=timeit.default_timer()
                mergesort(u)
                stop=timeit.default_timer()
                t+=stop-start
        mtimes.append(t/100)
        t=0
        for _ in range(100):
                np.random.permutation(u)
                start=timeit.default_timer()
                insertionsort(u)
                stop=timeit.default_timer()
                t+=stop-start
        itimes.append(t/100)
        t=0
        for _ in range(100):
                np.random.permutation(u)
                start=timeit.default_timer()
                selectionsort(u)
                stop=timeit.default_timer()
                t+=stop-start
        stimes.append(t/100)        
plt.plot([x for x in range(100,10300,300)],mtimes)	#mergesort first (blue)
plt.plot([x for x in range(100,10300,300)],itimes)	#insertionsort second(green)
plt.plot([x for x in range(100,10300,300)],stimes)	#selectionsort third (red)
plt.ylabel('Average Runtime')
plt.xlabel('Length of Array')
plt.title('All sorts average runtime on a randomized array')
plt.show()

'''
# All sorted and Backwards Sorted
msort=[]
munsort=[]
isort=[]
iunsort=[]
ssort=[]
sunsort=[]
for n in range(100,10300,300):
        s=np.array([x+1 for x in range(n)])
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        mergesort(s)
        stop=timeit.default_timer()
        msort.append(stop-start)
        start=timeit.default_timer()
        mergesort(u)
        stop=timeit.default_timer()
        munsort.append(stop-start)
        start=timeit.default_timer()
        insertionsort(s)
        stop=timeit.default_timer()
        isort.append(stop-start)
        start=timeit.default_timer()
        selectionsort(s)
        stop=timeit.default_timer()
        ssort.append(stop-start)
for n in range(100,10300,300):
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        selectionsort(u)
        stop=timeit.default_timer()
        sunsort.append(stop-start)
for n in range(100,10300,300):
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        insertionsort(u)
        stop=timeit.default_timer()
        iunsort.append(stop-start)

plt.plot([x for x in range(100,10300,300)], msort)
plt.plot([x for x in range(100,10300,300)],isort)
plt.plot([x for x in range(100,10300,300)],ssort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('All Sorts on a Sorted Array')
plt.show()


plt.plot([x for x in range(100,10300,300)], munsort)
plt.plot([x for x in range(100,10300,300)],iunsort)
plt.plot([x for x in range(100,10300,300)],sunsort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('All Sorts on a Backwards Sorted Array')
plt.show()
'''
'''
#selection sort on both 
isort=[]
iunsort=[]
for n in range(100,10300,300):
        s=np.array([x+1 for x in range(n)])
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        selectionsort(s)
        stop=timeit.default_timer()
        isort.append(stop-start)
        start=timeit.default_timer()
        selectionsort(u)
        stop=timeit.default_timer()
        iunsort.append(stop-start)
plt.plot([x for x in range(100,10300,300)], isort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Selection Sort on a Sorted Array')
plt.show()

plt.plot([x for x in range(100,10300,300)], iunsort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Selection Sort on a Backwards Sorted Array')
plt.show()

#mergeseort on both
msort=[]
munsort=[]
for n in range(100,10300,300):
        s=np.array([x+1 for x in range(n)])
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        mergesort(s)
        stop=timeit.default_timer()
        msort.append(stop-start)
        start=timeit.default_timer()
        mergesort(u)
        stop=timeit.default_timer()
        munsort.append(stop-start)
plt.plot([x for x in range(100,10300,300)], msort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Merge Sort on a Sorted Array')
plt.show()

plt.plot([x for x in range(100,10300,300)], munsort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Merge Sort on a Backwards Sorted Array')
plt.show()
'''
'''
#insertion on backwards - test 
isort=[]
iunsort=[]
for n in range(100,10300,300):
        s=np.array([x+1 for x in range(n)])
        u=np.array([n-x for x in range(n)])
        start=timeit.default_timer()
        insertionsort(s)
        stop=timeit.default_timer()
        isort.append(stop-start)
        start=timeit.default_timer()
        insertionsort(u)
        stop=timeit.default_timer()
        iunsort.append(stop-start)
plt.plot([x for x in range(100,10300,300)], isort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Insertion Sort on a Sorted Array')
plt.show()

plt.plot([x for x in range(100,10300,300)], iunsort)
plt.ylabel('Runtime')
plt.xlabel('Length of array')
plt.title('Insertion Sort on a Backwards Sorted Array')
plt.show()
'''
'''
plotfunct(selectionplot, sunsort)
plotfunct(selectionplot, ssort)
'''

















'''
        isort=[]
        iunsort=[]

        ##Insertion Sort
        for n in range(10**2, 10000, 100):
                s=np.array([x+1 for x in range(n)])
                u=np.array([n-x for x in range(n)])
                start=timeit.default_timer()
                insertionsort(s)
                stop=timeit.default_timer()
                isort.append(stop-start)
                start=timeit.default_timer()
                insertionsort(u)
                stop=timeit.default_timer()
                iunsort.append(stop-start)
        ##selectionsort
        ssort=[]
        sunsort=[]
        for n in range(10**2):
                s=np.array(([x+1 for x in range(n)])
                u=np.array([n-x for x in range(n)])
                start=timeit.default_timer()
                selectionsort(s)
                stop=timeit.default_timer()
                selectionsort(u)
                stop=timeit.default_timer()
                sunsort.append(stop-start)
        #mergesort (not working...)

        msort=[]
        munsort=[]
        for n in range(10**2):
                s=np.array([x+1 for x in range(n)])
                u=np.array([n-x for x in range(n)])
                start=timeit.default_timer()
                mergesort(s)
                stop=timeit.default_timer()
                msort.append(stop-start)
                start=timeit.default_timer()
                mergesort(u)
                stop=timeit.default_timer()
                munsort.append(stop-start)

        selectionplot = PdfPages('selection.pdf')#make insertion sort plot
        insertplot = PdfPages('insertion.pdf')
        mergeplot = PdfPages('merge.pdf')
        unsortplot = PdfPages('all-unsorted.pdf')
        sortplot = PdfPages('all-sorted.pdf')
                           
                           
        def plotfunct(plotname, Type):
                
                plt.plot(Type)  # ?
                plt.ylabel('Runtime')
                plt.xlabel('length')
                #plt.show() #NOT SURE IF THIS IS NEEDED
                plotname.savefig()

        plotfunct(selectionplot, sunsort)
        plotfunct(selectionplot, ssort)

        plotfunct(insertplot, iunsort)
        plotfunct(insertplot, isort)
                           
        plotfunct(mergeplot, munsort)
        plotfunct(mergeplot, msort)

        plotfunct(unsortplot, sunsort)
        plotfunct(unsortplot, iunsort)
        plotfunct(unsortplot, munsort)

        plotfunct(sortplot, ssort)
        plotfunct(sortplot, isort)
        plotfunct(sortplot, msort)

        selectionplot.close()
        insertplot.close()
        mergeplot.close()
        unsortplot.close()
        sortplot.close()
                
'''