# 1. 하나의 연산 중 가장 큰 값을 갖는 i를 선택한다
# 2. 가장 큰 값을 가지는 'arg1 operator arg2' i가 두개 이상인 경우, 연산자 우선순위가 높은 i를 선택한다.
# 3. i가 가장 큰 값을 가지고 연산자가 2개 이상인데 우선순위가 같은 경우 i가 가장 작은 것을 선택한다.
# 4. i를 먼저 계산하고 연산자 개수만큼 반복한다.

# 여기서 /는 C++ 기준으로 몫 나누기 이므로 파이썬에서는 /연산자를 쓰되 int형으로 형 변환하는 방법을 쓰겠음.


def calculator(arg1, operator, arg2):
    if operator == '+':
        return arg1 + arg2
    elif operator == '-':
        return arg1 - arg2
    elif operator == '*':
        return arg1 * arg2
    else:
        return int(arg1 / arg2)

values = input()
values_split = []

done = 0
for i, value in enumerate(values):
    if value in ['+', '-', '*', '/']:
        arg = int(values[done:i])
        values_split.append(arg)
        done = i + 1
        values_split.append(value)

values_split.append(int(values[done:]))

if len(values_split) == 1:
    print(values_split[0])
else:
    indexs_operator = [i for i, value in enumerate(values_split) if value in ['+', '-', '*', '/']]

    op_priority = {'*': 2, '/': 2, '+': 1, '-': 1}

    while indexs_operator:
        max_value = float('-inf')
        max_index = -1

        for i in indexs_operator:
            op = values_split[i]
            val1 = values_split[i - 1]
            val2 = values_split[i + 1]
            temp_result = calculator(val1, op, val2)

            if temp_result > max_value or (temp_result == max_value and op_priority[op] > op_priority[values_split[max_index]]):
                max_value = temp_result
                max_index = i

        result = calculator(values_split[max_index - 1], values_split[max_index], values_split[max_index + 1])
        values_split[max_index - 1] = result
        del values_split[max_index:max_index + 2]
        indexs_operator = [i for i, value in enumerate(values_split) if value in ['+', '-', '*', '/']]

    print(values_split[0])
