def hanoi(N,A,B,C):
    if N ==1:
        print(A,C)
        return
    hanoi(N-1,A,C,B)
    print(A,C)
    hanoi(N-1,B,A,C)


N = (int)(input())

sum=1
for i in range(N - 1):
    sum = sum * 2 + 1

print(sum)
hanoi(N,1,2,3)