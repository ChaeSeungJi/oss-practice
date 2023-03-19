# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.




list_s = []

N = (int)(input())

list_s = list(map(int,input().split()))
list_copy = list_s[:]
list_result = [0]*N

list_s.sort()
count=0
previous_index_value = None
previous_count = 0


for i in range(N):
    j=0
    for element in list_copy:
        if(list_s[0] == element):
            if(previous_index_value == list_s[0]):
                list_result[j] = previous_count
                if(list_s[0] != None): list_s.pop(0)
                list_copy[j]=None
                break
            else:
                list_result[j] = count
                previous_index_value = list_s[0]
                previous_count = count
                if(list_s[0] != None): list_s.pop(0)
                count +=1
                list_copy[j]=None
                break
        j+=1


print(*list_result)

# def coordinate_compression(arr):
#     sorted_arr = sorted(set(arr))  # 중복 제거 및 정렬
#     dict = {value: index for index, value in enumerate(sorted_arr)}  # 각 원소의 인덱스를 저장
#     return [dict[value] for value in arr]  # 인덱스로 변환된 결과를 반환


# N = (int)(input())
# # 예시 입력
# arr = list(map(int,input().split()))
# # 좌표 압축 적용
# compressed_arr = coordinate_compression(arr)
# # 결과 출력
# print(*compressed_arr)