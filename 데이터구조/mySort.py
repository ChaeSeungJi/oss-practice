import sys
import random
import time

sys.setrecursionlimit(100000)
listLength = 300
my_list = []

# 리스트 생성 함수
def make_lsit(a: list):
    for i in range(listLength):
        a.append(random.randint(0, 100))  # 0부터 100까지의 난수 추가

# 버블정렬 (재귀적)
def bubbleSortRec(A, n):
    for i in range(n-1):  # 리스트의 마지막 전 요소까지 반복
        if A[i] > A[i+1]:  # 현재 요소가 다음 요소보다 크다면
            A[i], A[i+1] = A[i+1], A[i]  # 현재 요소와 다음 요소를 교환
    if n > 1:  # n이 1보다 크다면
        bubbleSortRec(A, n-1)  # n-1로 재귀 호출

# 선택정렬 (재귀적)
def selectionSortRec(arr, start=0):
    if start >= len(arr) - 1:  # 시작 인덱스가 리스트 길이보다 크거나 같으면 종료
        return

    min_index = start  # 최소값 인덱스를 시작 인덱스로 초기화
    for i in range(start + 1, len(arr)):  # 시작 인덱스 다음부터 리스트 끝까지 반복
        if arr[i] < arr[min_index]:  # 현재 요소가 최소값보다 작으면
            min_index = i  # 최소값 인덱스를 현재 요소의 인덱스로 업데이트

    # 최소값 요소와 시작 인덱스의 요소를 교환
    arr[start], arr[min_index] = arr[min_index], arr[start]

    selectionSortRec(arr, start + 1)  # 다음 인덱스부터 정렬 시작 (재귀 호출)

# 삽입정렬 (재귀적)
def insertionSortRec(A, start, end):
    value = A[start]  # 시작 인덱스의 값을 저장
    loc = start  # 시작 인덱스를 loc 변수에 저장

    # loc이 0보다 크고 이전 요소가 value보다 크면 반복
    while loc > 0 and A[loc-1] > value:
        A[loc] = A[loc-1]  # 이전 요소를 현재 요소로 이동
        loc -= 1  # loc 값을 1 감소시킴

    A[loc] = value  # 현재 요소에 value 값 저장

    if start + 1 < end:  # 다음 인덱스가 리스트의 끝이 아니라면
        insertionSortRec(A, start+1, end)  # 다음 인덱스부터 정렬 시작 (재귀 호출)

# 병합정렬 (재귀적)
def mergeSortRec(A, B, p: int, r: int):
    if p < r:  # 시작 인덱스가 끝 인덱스보다 작으면
        q = (p + r) // 2  # 중간 인덱스 계산
        mergeSortRec(A, B, p, q)  # 시작 인덱스부터 중간 인덱스까지 재귀 호출
        mergeSortRec(A, B, q + 1, r)  # 중간 인덱스 다음부터 끝 인덱스까지 재귀 호출
        merge(A, B, p, q, r)  # 병합 실행

# 병합 함수
def merge(A: list, B: list, p: int, q: int, r: int):
    i = p  # 시작 인덱스 저장
    j = q + 1  # 중간 다음 인덱스 저장
    t = 0  # 임시 인덱스 초기화

    # 시작 인덱스가 중간 인덱스 이하이고 중간 다음 인덱스가 끝 인덱스 이하인 동안 반복
    while i <= q and j <= r:
        if A[i] <= A[j]:  # 현재 인덱스의 값이 중간 다음 인덱스의 값보다 작거나 같으면
            B[t] = A[i]  # 임시 리스트에 현재 인덱스의 값을 추가
            t += 1  # 임시 인덱스 증가
            i += 1  # 현재 인덱스 증가
        else:  # 중간 다음 인덱스의 값이 더 작으면
            B[t] = A[j]  # 임시 리스트에 중간 다음 인덱스의 값을 추가
            t += 1  # 임시 인덱스 증가
            j += 1  # 중간 다음 인덱스 증가

    # 시작 인덱스가 중간 인덱스 이하인 동안 반복
    while i <= q:
        B[t] = A[i]  # 임시 리스트에 현재 인덱스의 값을 추가
        t += 1  # 임시 인덱스 증가
        i += 1  # 현재 인덱스 증가

    # 중간 다음 인덱스가 끝 인덱스 이하인 동안 반복
    while j <= r:
        B[t] = A[j]  # 임시 리스트에 중간 다음 인덱스의 값을 추가
        t += 1  # 임시 인덱스 증가
        j += 1  # 중간 다음 인덱스 증가

    A = B.copy()  # 임시 리스트를 원본 리스트에 복사

# 퀵정렬
def partition(arr, low, high):
    pivot = arr[high]  # 피봇 값 설정
    i = low - 1  # i 초기화

    for j in range(low, high): # 리스트의 시작부터 끝 전까지 반복
        if arr[j] <= pivot:  # 현재 원소가 피봇 값보다 작거나 같으면
            i += 1  # i를 증가시킴
            arr[i], arr[j] = arr[j], arr[i]  # 현재 원소와 i 위치의 원소를 교환

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 피봇 값과 i + 1 위치의 원소를 교환
    return i + 1  # 피봇의 새로운 위치 반환

def quick_sort(arr, low, high):
    if low < high:  # 시작 인덱스가 끝 인덱스보다 작으면
        pi = partition(arr, low, high)  # 피봇 위치 설정

        quick_sort(arr, low, pi - 1)  # 피봇 이전 부분 정렬
        quick_sort(arr, pi + 1, high)  # 피봇 이후 부분 정렬

# 힙정렬
def buildHeap(A):
    for i in range((len(A) - 2) // 2, -1, -1):  # 배열의 중간부터 시작하여 역순으로 반복
        perecolateDown(A, i, len(A) - 1)  # 하향식 힙 생성

def perecolateDown(A, k: int, end: int):
    child = 2 * k + 1  # 왼쪽 자식 인덱스 계산
    right = 2 * k + 2  # 오른쪽 자식 인덱스 계산
    if child <= end:  # 왼쪽 자식 인덱스가 배열 크기보다 작으면
        if right <= end and A[child] < A[right]:  # 오른쪽 자식 인덱스가 배열 크기보다 작고 왼쪽 자식보다 크면
            child = right  # 오른쪽 자식을 선택
        if A[k] < A[child]:  # 부모가 선택한 자식보다 작으면
            A[k], A[child] = A[child], A[k]  # 부모와 자식의 값을 교환
            perecolateDown(A, child, end)  # 자식 위치에서 다시 하향식 힙 생성 실행

def heap_sort(A):
    buildHeap(A)  # 힙 생성
    for last in range(len(A) - 1, 0, -1):  # 배열 끝부터 시작하여 역순으로 반복
        A[last], A[0] = A[0], A[last]  # 최대값(힙의 루트)와 배열의 마지막 값을 교환
        perecolateDown(A, 0, last - 1)  # 변경된 배열에서 다시 하향식 힙 생성 실행

# 쉘정렬
def shellSort(A):
    H = gapSquence(len(A))  # 간격 시퀀스 계산
    for h in H:  # 간격 시퀀스에 따라 반복
        for k in range(h):  # 각 간격에서 시작하는 부분 배열에 대해
            stepInsertionSort(A, k, h)  # 간격별 삽입 정렬 실행

def stepInsertionSort(A, k: int, h: int):
    for i in range(k + h, len(A), h):  # 간격 h만큼 건너뛰며 반복
        j = i - h  # 이전 인덱스 계산
        newItem = A[i]  # 현재 원소 저장
        while 0 <= j and newItem < A[j]:  # 이전 인덱스가 0 이상이고 현재 원소가 이전 원소보다 작으면
            A[j + h] = A[j]  # 이전 원소를 간격 h만큼 앞으로 옮김
            j -= h  # 이전 인덱스를 간격 h만큼 뒤로 이동
        A[j + h] = newItem  # 현재 원소를 올바른 위치에 삽입

def gapSquence(n: int):
    H = [1]  # 간격 시퀀스 초기화
    gap = 1  # 초기 간격 설정
    while gap < n / 5:  # 간격이 배열 크기의 1/5보다 작은 동안
        gap = 3 * gap + 1  # 간격을 3배하고 1을 더함
        H.append(gap)  # 새로운 간격을 시퀀스에 추가
    H.reverse()  # 간격 시퀀스를 역순으로 정렬
    return H  # 간격 시퀀스 반환

def startTest():
    sum_bubble = 0  # 버블정렬의 시간을저장하기 위한 변수
    sum_selection = 0  # 선택정렬의 시간을저장하기 위한 변수
    sum_insertion = 0   # 삽입정렬의 시간을저장하기 위한 변수
    sum_merge = 0   # 병합정렬의 시간을저장하기 위한 변수
    sum_quick = 0   # 퀵정렬의 시간을저장하기 위한 변수
    sum_heap = 0    # 힙정렬의 시간을저장하기 위한 변수
    sum_shell = 0   # 쉘정렬의 시간을저장하기 위한 변수

    count = 1000    

    for i in range(count):# 1000회 반복
        my_list.clear() # my_list비우기
        make_lsit(my_list) # my_list채우기

        start = time.time() # 시작시간
        bubbleSortRec(my_list.copy(), listLength) # 버블정렬 실행
        end = time.time()   # 종료시간
        sum_bubble += end - start # 변수에 함수 동작시간 더하기

        start = time.time() # 시작시간
        selectionSortRec(my_list.copy())    # 선택정렬 실행
        end = time.time()   # 종료시간
        sum_selection += end - start    # 변수에 함수 동작시간 더하기


        start = time.time() # 시작시간
        insertionSortRec(my_list.copy(), 1, listLength-1)   # 삽입정렬 실행
        end = time.time()   # 종료시간
        sum_insertion += end - start    # 변수에 함수 동작시간 더하기


        start = time.time() # 시작시간
        C = [None] * listLength # 병합정렬의 출력값을 위한 변수 빈 리스트
        mergeSortRec(my_list.copy(), C, 0, listLength-1)    # 병합정렬 실행
        end = time.time()   # 종료시간
        sum_merge += end - start    # 변수에 함수 동작시간 더하기


        start = time.time() # 시작시간
        quick_sort(my_list.copy(), 0, listLength-1) # 퀵정렬 실행
        end = time.time()   # 종료시간  # 변수에 함수 동작시간 더하기
        sum_quick += end - start

        start = time.time() # 시작시간
        heap_sort(my_list.copy())   # 힙정렬 실행
        end = time.time()   # 종료시간  
        sum_heap += end - start # 변수에 함수 동작시간 더하기

        start = time.time() # 시작시간
        shellSort(my_list.copy())   # 쉘정렬 실행
        end = time.time()   # 종료시간
        sum_shell += end - start    # 변수에 함수 동작시간 더하기


    print("버블정렬의 평균 : ", sum_bubble/count)
    print("선택정렬의 평균 : ", sum_selection/count)
    print("삽입정렬의 평균 : ", sum_insertion/count)
    print("병합정렬의 평균 : ", sum_merge/count)
    print("  퀵정렬의 평균 : ", sum_quick/count)
    print("  힙정렬의 평균 : ", sum_heap/count)
    print("  쉘정렬의 평균 : ", sum_shell/count)



startTest()

