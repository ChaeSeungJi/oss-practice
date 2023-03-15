# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# <입력>

# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# <출력>

# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# import sys
# input = sys.stdin.readline().rstrip()


def return_value(tuple_):
    x,y=tuple_
    return str(x) + " " + str(y)

N=int(input())
coordinates =  []

for i in range(N):
    x,y = list(map(int,input().split()))
    t = (x,y)
    coordinates.append(t)

sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[1],coord[0]))

for i in range(N):
    print(return_value(sorted_coordinates[i]))






