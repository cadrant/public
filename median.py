#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#
import random

def partition(L,v):
    smaller = []
    bigger= []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return (smaller, [v], bigger)

def top_k(L,k):
    v = L[random.randrange(len(L))]
    (left,middle,right) = partition(L,v)
    if len(left) == k: return left
    if len(left) + 1 == k: return left + [v]
    if len(left) > k: return top_k(left,k)
    return left+[v]+top_k(right,k-len(left)-1)

def minimize_absolute(L):
    x = 0
    # your code here
    if(len(L) % 2):
        klist = top_k(L,len(L)/2+1)
        print klist
        median = klist[len(klist)-1] + klist[len(klist)-2] /2 
    else:
        klist = top_k(L,len(L)/2)
        print klist
        median = klist[len(klist)-1] 
    return median
    
def test():
    L = [1,2,3,4,5,5,5,5,5,5]
    print minimize_absolute(L)
    L = [1,2,3]
    print minimize_absolute(L)
    
test()

