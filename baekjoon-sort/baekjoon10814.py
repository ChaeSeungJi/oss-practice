
# 1. 튜플로 순서 , 나이 , 이름을 받는다.
# 2. 순서와 나이로 정렬한다.
# 3. 순서를 삭제한다.

list_s = []

N = (int)(input())

for i in range(N):
    list_tmp = input().split()
    tuple_s = (i, (int)(list_tmp[0]), list_tmp[1])
    list_s.append(tuple_s)

list_s.sort(key=lambda element: (element[1], element[0]))

for s in list_s:
    print(s[1],s[2])
