array = list(map(int, input().split()))

def parent(i):
    return i//2

def left(i):
    return (i+1) * 2 - 1

def right(i):
    return (i+1) * 2 

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    largest = None
    print(i, l, r)
    if l <= len(A)-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= len(A)-1 and A[r] > A[largest]:
        largest = r

    if largest != i:
        a =  A[i]
        A[i] = A[largest]
        A[largest] = a
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        print(i)
        max_heapify(A, i)
    print(A)

build_max_heap(array)
