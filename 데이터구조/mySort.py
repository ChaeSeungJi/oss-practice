import sys
import random
import time

sys.setrecursionlimit(100000)
listLength = 300 # 기본 300
my_list = []


def make_lsit(a: list):
    for i in range(listLength):
        a.append(random.randint(0, 100))


def bubbleSortRec(A, n):
    for i in range(n-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
    if n > 1:
        bubbleSortRec(A, n-1)


def selectionSortRec(arr, start=0):
    if start >= len(arr) - 1:
        return

    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i

    arr[start], arr[min_index] = arr[min_index], arr[start]

    selectionSortRec(arr, start + 1)


def insertionSortRec(A, start, end):
    value = A[start]
    loc = start
    while loc > 0 and A[loc-1] > value:
        A[loc] = A[loc-1]
        loc -= 1
    A[loc] = value

    if start + 1 < end:
        insertionSortRec(A, start+1, end)


def mergeSortRec(A, B, p: int, r: int):
    if p < r:
        q = (p+r)//2
        mergeSortRec(A, B, p, q)
        mergeSortRec(A, B, q+1, r)
        merge(A, B, p, q, r)


def merge(A: list, B: list, p: int, q: int, r: int):
    i = p
    j = q+1
    t = 0
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B[t] = A[i]
            t += 1
            i += 1
        else:
            B[t] = A[j]
            t += 1
            j += 1
    while i <= q:
        B[t] = A[i]
        t += 1
        i += 1
    while j <= r:
        B[t] = A[j]
        t += 1
        j += 1
    A = B.copy()



def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)



# make_lsit(my_list)
# # copy_list = my_list.copy()

# start = time.time()
# bubbleSortRec(my_list.copy(), listLength)
# end = time.time()
# print("버블정렬 : ", end - start, "sec")


# start = time.time()
# selectionSortRec(my_list.copy())
# end = time.time()

# print("선택정렬 : ", end - start, "sec")


# start = time.time()
# insertionSortRec(my_list.copy(), 1, listLength-1)
# end = time.time()

# print("삽입정렬 : ", end - start, "sec")


# start = time.time()
# C = [None] * listLength
# mergeSortRec(my_list.copy(), C, 0, listLength-1)
# end = time.time()

# print("병합정렬 : ", end - start, "sec")


sum_bubble = 0
sum_selection = 0
sum_insertion = 0
sum_merge = 0
sum_quick = 0
sum_heap = 0



count = 1000

for i in range(count):
    my_list.clear()
    make_lsit(my_list)

    start = time.time()
    bubbleSortRec(my_list.copy(), listLength)
    end = time.time()
    sum_bubble += end - start

    start = time.time()
    selectionSortRec(my_list.copy())
    end = time.time()
    sum_selection += end - start


    start = time.time()
    insertionSortRec(my_list.copy(), 1, listLength-1)
    end = time.time()
    sum_insertion += end - start


    start = time.time()
    C = [None] * listLength
    mergeSortRec(my_list.copy(), C, 0, listLength-1)
    end = time.time()
    sum_merge += end - start


    start = time.time()
    quick_sort(my_list.copy(), 0, listLength-1)
    end = time.time()ㅇ
    sum_quick += end - start

    start = time.time()
    heap_sort(my_list.copy())
    end = time.time()
    sum_heap += end - start


print("버블정렬의 평균 : ", sum_bubble/count)
print("선택정렬의 평균 : ", sum_selection/count)
print("삽입정렬의 평균 : ", sum_insertion/count)
print("병합정렬의 평균 : ", sum_merge/count)
print("  퀵정렬의 평균 : ", sum_quick/count)
print("  힙정렬의 평균 : ", sum_heap/count)

