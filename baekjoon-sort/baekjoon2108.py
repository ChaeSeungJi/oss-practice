# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.


# <입력>

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.


# <출력>

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

# 둘째 줄에는 중앙값을 출력한다.

# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 넷째 줄에는 범위를 출력한다.

import sys
import math

n = int(sys.stdin.readline())
array_int = [0]*4001
sum = 0

for i in range(n):
    value = int(sys.stdin.readline())
    sum += value
    array_int[value] += 1

average = sum/n
median_value = 0
median_count = 0
dictionary_int = {}
start = 0
last = 0

for i in range(4001):
    # i가 실제 값
    temp = array_int[i]     # temp = 빈도
    if (temp != 0):
        median_count += 1
        if (median_count == n/2+1):
            median_value = i

        if (start == 0):
            start = i
        last = i
        dictionary_int[i] = temp

print(round(average))
print(median_value)
print(max(dictionary_int.values()))
print(last-start)


# ===========================================================================

from collections import Counter

# input
n = int(input())

# initialize variables
sum_vals = 0
max_val = -4000
min_val = 4000
counts = [0] * 8001

# calculate statistics
for i in range(n):
    num = int(input())
    sum_vals += num
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
    counts[num + 4000] += 1

# arithmetic mean
mean = sum_vals / n
print(round(mean, 1))

# median
median_idx = (n - 1) // 2
count_sum = 0
median = 0
for i, count in enumerate(counts):
    count_sum += count
    if count_sum > median_idx:
        median = i - 4000
        break
    elif count_sum == median_idx and n % 2 == 0:    # 짝수일 때
        for j in range(i + 1, 8001):
            if counts[j] > 0:
                median = (i + j - 8000) / 2
                break
        break
print(median)

# mode
max_freq = max(counts)
modes = [i - 4000 for i, count in enumerate(counts) if count == max_freq]
mode = min(modes) if len(modes) == 1 else sorted(modes)[1]
print(mode)

# range
range_val = max_val - min_val
print(range_val)



# =================================================
from collections import Counter

# input
n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)

# arithmetic mean
mean = sum(nums) / n
print(round(mean, 1))

# median
nums.sort()
median = nums[n // 2]
print(median)

# mode
freqs = Counter(nums)
max_freq = max(freqs.values())
modes = [num for num, freq in freqs.items() if freq == max_freq]
mode = min(modes) if len(modes) == 1 else sorted(modes)[1]
print(mode)

# range
range_val = max(nums) - min(nums)
print(range_val)