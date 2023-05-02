import sys
import random
import time

sys.setrecursionlimit(100000)
listLength = 300
my_list = []


def make_lsit(a: list):
    for i in range(300):
        a.append(random.randint(0, 100))


def bubbleSortRec(A, n):
    for i in range(n-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
    if n > 1:
        bubbleSortRec(A, n-1)


def selectionSortRec(A):
    if A != []:
        x = max(A)
        A.remove(x)
        return selectionSortRec(A) + [x]
    else:
        return []


def insertionSortRec(A, start, end):
    value = A[start]
    loc = start
    while loc > 0 and A[loc-1] > value:
        A[loc] = A[loc-1]
        loc -= 1
    A[loc] = value

    if start + 1 < end:
        insertionSortRec(A, start+1, end)


def mergeSortRec(A,B,p:int,r:int):
    if p<r:
        q = (q+r)//2
        mergeSortRec(A,B,p,q)
        mergeSortRec(A,B,q+1,r)
        merge(A,B,p,q,r)

def merge(A:list,B:list,p:int,q:int,r:int):
    i=p;j=q+1;t=0
    while i<=q and j<=r:
        if A[i] <=A[j]:
            B[t] = A[i]; t += 1; i+=1
        else:
            B[t] = A[j]; t+=1; j+=1
    while i<=q:
        B[t]=A[i]; t+=1; i+=1
    while j<=r:
        B[t] = A[j]; t+=1; j+=1
    A = B.copy()


make_lsit(my_list)
# copy_list = my_list.copy()

start = time.time()
bubbleSortRec(my_list.copy(), listLength)
end = time.time()
print("버블정렬 : ", end - start, "sec")


start = time.time()
selectionSortRec(my_list.copy())
end = time.time()

print("선택정렬 : ", end - start, "sec")


start = time.time()
insertionSortRec(my_list.copy(),1,listLength-1)
end = time.time()

print("삽입정렬 : ", end - start, "sec")
