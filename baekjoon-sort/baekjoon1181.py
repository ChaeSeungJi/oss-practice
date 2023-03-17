

list_s = []

N = (int)(input())

for i in range(N):
    list_s.append(input())


set_s = set(list_s) # set자료구조의 특징인 중복이 없다는 성질을 이용

list_s=list(set_s)
list_s.sort()
list_s.sort(key=lambda element: len(element))

for s in list_s:
    print(s)
