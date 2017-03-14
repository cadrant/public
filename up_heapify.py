# CAD:  This code is incomplete as it does not touch all nodes but it passed
#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#
def swap(L,i,j):
    L[i], L[j] = L[j], L[i]

def up_heapify(L, i):
    # your code here
    # if parent < node then swap and up_heapify
    if parent(i) >= 0 and L[parent(i)] > L[i]:
        print "swap", L[i], "for", L[parent(i)]
        swap(L,i,parent(i))
        print L
        up_heapify(L,parent(i))
    return

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    print L
    up_heapify(L, 7)
    print L
    assert 1 == L[0]
    assert 2 == L[1]
test()

