import re

# logic_symbols = {"and": "∧", "or": "∨", "~": "¬", "$": "→"}
list_logicOperator = ["∧", "∨"]
list_logicSymbol = ["¬", "→"]

# 후위표현법으로 변환
def infix_to_postfix(expression):
    precedence = {"∧": 2, "∨": 1}
    stack = []
    postfix = []
    expression = ' '.join(expression)
    for token in expression.split():
        if token in precedence:  # token이 연산자인 경우
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                postfix.append(stack.pop())
            stack.append(token)
        else:  # token이 피연산자인 경우
            postfix.append(token)

    while stack:
        postfix.append(stack.pop())

    return postfix

# 중위표현법으로 변환 괄호와 함께
def postfix_to_infix(expression):
    stack = []
    expression = ' '.join(expression)
    for token in expression.split():
        if token in ["∧", "∨"]:  # token이 연산자인 경우
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"({operand1} {token} {operand2})")
        else:  # token이 피연산자인 경우
            stack.append(token)

    return stack[0]

# 요소들을 다른 이름으로 변환
def convert(expression):
    ch = 97
    expression = list(expression)
    for i, value in enumerate(expression):
        if value == list_logicOperator[0] or value == list_logicOperator[1]:
            continue
        expression[i] = chr(ch)
        ch += 1
    return expression

def convert2(expression,dic):
    ch = 97
    dic2={}
    for v in dic:
        list=[]
        ch2=97
        for i in range(dic[v]):
            list.append(chr(ch)+chr(ch2))
            ch2 += 1
        dic2[v]=list
        ch += 1

    for i,v in enumerate(expression):
        if v == list_logicOperator[0] or v == list_logicOperator[1]:
            continue
        if v in dic2:
            expression[i] = dic2[v].pop(0)
    return expression


def stringToList(String):
    return [part.strip() for part in String.split()]


# coffee를 a로 간단화하는 과정, 입력 expression은 list임
def Translation(expression,dic):
    expression = infix_to_postfix(expression) # 후위표현법
    expression = convert2(expression,dic)
    expression = postfix_to_infix(expression) # 문자열 상태,중위표현법
    return expression

# 리스트에서 같은 문자열을 카운트해서 딕셔너리로 반환한다.
def countOverlappingString(li:list):
    s1 = set(li)
    s1.discard("∧")
    s1.discard("∨")
    dic={}
    for v in s1:
        dic[v]=0
    for v in li:
        if v in s1:
            dic[v] += 1
    return dic


#

# 여기서부터는 메인 내용
inputString = "coffee ∧ coffee ∨ tea → coffee ∨ coffee"
logics = inputString.split("→")
leftLogic = logics[0]
leftLogic = stringToList(leftLogic)
rightLogic = logics[1]
rightLogic = stringToList(rightLogic)

dicleft = countOverlappingString(leftLogic)
leftLogic = Translation(leftLogic,dicleft)

dicright = countOverlappingString(rightLogic)
rightLogic = Translation(rightLogic,dicright)
completely_expression = leftLogic + " → " + rightLogic
print(completely_expression)

# To do list
# 1. not 연산자는 어떻게 처리할 지
# 2. 크롤링이용해서 값 가져오기
