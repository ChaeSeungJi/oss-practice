import sys
n=int(sys.stdin.readline())
array_int =[0]*10001

for i in range(n):
    array_int[int(sys.stdin.readline())] += 1


for i in range(10001):
    temp = array_int[i]
    if temp != 0:
        for j in range(temp):
            print(i)