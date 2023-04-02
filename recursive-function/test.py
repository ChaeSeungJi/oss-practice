import sys
import re
import heapq

input = sys.stdin.readline

expression = input().rstrip()
operands = list(map(int, re.findall(r'\d+', expression)))  # \d를 사용해서 숫자만 추출
operators = re.findall(r'\D', expression)   # \D를 사용해서 문자만 추출

answer = operands[0]
maxHeap = []
expression_info = dict()


def get_operator_priority(operator):
    return -1 if operator in ['*', '/'] else 0


def evaluate_expression(index):
    num1, num2, operator, _, _ = expression_info[index]
    return operator_dict[operator](num1, num2)


operator_dict = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x // y}

for i in range(1, len(operands)):
    # key : i-1, value : tuple(인자, 연산자, 인자2, 왼쪽연산자 idx, 오른쪽연산자 idx)
    expression_info[i-1] = (operands[i-1], operands[i], operators[i-1], i-2, i)
    # 람다 함수를 통해 계산한 결과를 value에 저장
    value = operator_dict[operators[i-1]](operands[i-1], operands[i])

    # 작은 것이 우선순위가 높아지는 최대힙 특성을 고려하여 value 부호를 바꿔줌.    
    # -value, 연산자 우선순위, 연산자idx를 튜플로 만들어서 최대힙에다가 넣음. 튜플 인자 순서대로 우선순위가 높음
    heapq.heappush(maxHeap, (-value, get_operator_priority(operators[i-1]), i-1))

while maxHeap:
    value, _, index = heapq.heappop(maxHeap) # 힙에서 우선순위가 높은것을 뺴옴.

    # 값이 진짜 최댓값인지 확인하는 과정. 위에서 value의 부호를 -로 했기 때문에, 힙에서 우선순위가 높다고 최댓값이 아닐수도 있음.
    evaluate_value = evaluate_expression(index) 

    if -value == evaluate_value:    # 진짜 최댓값이 맞으면
        answer = evaluate_value
        left_expression = expression_info[index][3] # 왼쪽연산자idx
        right_expression = expression_info[index][4] # 오른쪽연산자idx

        if left_expression > -1: # 왼쪽연산자에 값이 없는 경우만 아니면

            # 계산한 결과가 새로운 인자가 되고 양 옆 연사자들을 붙여줌
            expression_info[left_expression] = (expression_info[left_expression][0], evaluate_value,
                                                expression_info[left_expression][2], expression_info[left_expression][3], right_expression)
            
            left_value = evaluate_expression(left_expression) # 힙에서 추출한 결과와 왼쪽 연산자 인자를 계산함

            # left_value를 힙에다가 갱신함.
            heapq.heappush(maxHeap, (-left_value, get_operator_priority(
                expression_info[left_expression][2]), left_expression))
        
        # if왼쪽과 똑같이 오른쪽에 대해서도 추가함.
        if right_expression < len(expression_info): # 오른쪾 연산자에 값이 없는 경우만 아니면
            expression_info[right_expression] = (evaluate_value, expression_info[right_expression][1],
                                                 expression_info[right_expression][2], left_expression, expression_info[right_expression][4])
            right_value = evaluate_expression(right_expression)
            heapq.heappush(maxHeap, (-right_value, get_operator_priority(
                expression_info[right_expression][2]), right_expression))
            
            # 이 과정을 계산하고 계속 게산해서 힙에 아무 값도 없을 때까지 반복함.

print(answer)
