import sys
import re
import heapq
input = sys.stdin.readline

exp = input().rstrip()
nums = list(map(int, re.split(r'\*|/|\+|-', exp)))
oper = list(re.sub(r'[0-9]', '', exp))

answer = nums[0]
pq = []
oper_info = dict()
for i in range(1, len(nums)):
    # 연산자 정보 (좌, 우 숫자, 자신의 연산기호, 내 왼쪽의 연산자 번호, 내 오른쪽의 연산자 번호) 저장
    oper_info[i-1] = ([nums[i-1], nums[i], oper[i-1], i-2, i])

    # 우선순위 큐에 저장할 연산결과값, 연산자 우선순위, 인덱스 계산
    oper_prior = -1 if oper[i-1] == '*' or oper[i-1] == '/' else 0
    if oper[i-1] == '*':
        value = nums[i-1] * nums[i]
    elif oper[i-1] == '/':
        value = nums[i-1] // nums[i]
    elif oper[i-1] == '+':
        value = nums[i-1] + nums[i]
    elif oper[i-1] == '-':
        value = nums[i-1] - nums[i]
    else:
        raise Exception("wrong operator")

    heapq.heappush(pq, (-value, oper_prior, i-1))


def checkValue(index):
    if oper_info[index][2] == '+':
        return oper_info[index][0] + oper_info[index][1]
    elif oper_info[index][2] == '-':
        return oper_info[index][0] - oper_info[index][1]
    elif oper_info[index][2] == '*':
        return oper_info[index][0] * oper_info[index][1]
    else:
        ### 음수에 대한 몫 계산 처리 필요
        return oper_info[index][0] // oper_info[index][1]

while pq:
    get_value, prior, index = heapq.heappop(pq)

    # 현재 연산자 정보의 값과 pq 값이 일치하면, 최신 값을 꺼낸 것으로 본다. (검증 필요, 값이 겹칠 수 있으므로)
    check_value = checkValue(index)
    if -get_value == check_value:
        answer = check_value

        left_oper = oper_info[index][3]
        right_oper = oper_info[index][4]

        # 내 왼쪽 연산자에 대해
        if left_oper > -1:
            # 오른쪽 피연산자를 결과값으로 바꿔준다.
            oper_info[left_oper][1] = check_value
            # 오른쪽으로 연결된 연산자를 내 오른쪽 연산자로 바꿔준다.
            oper_info[left_oper][4] = right_oper
            # 바꾼 피연산자로 계산한 값을 pq에 넣어준다.
            left_change_value = checkValue(left_oper)
            if oper_info[left_oper][2] == '*' or oper_info[left_oper][2] == '/':
                left_operator = -1
            else:
                left_operator = 0
            heapq.heappush(pq, (-left_change_value, left_operator, left_oper))

        # 내 오른쪽 연산자에 대해
        if right_oper < len(oper_info):
            # 왼쪽 피연산자를 결과값으로 바꿔준다.
            oper_info[right_oper][0] = check_value
            # 왼쪽으로 연결된 연산자를 내 왼쪽 연산자로 바꿔준다.
            oper_info[right_oper][3] = left_oper
            # 바꾼 피연산자로 계산한 값을 pq에 넣어준다.
            right_change_value = checkValue(right_oper)
            if oper_info[right_oper][2] == '*' or oper_info[right_oper][2] == '/':
                right_operator = -1
            else:
                right_operator = 0
            heapq.heappush(pq, (-right_change_value, right_operator, right_oper))

print(answer)