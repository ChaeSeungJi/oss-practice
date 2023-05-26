import re

# logic_symbols = {"and": "∧", "or": "∨", "~": "¬", "$": "→"}
list_logicOperator = ["∧", "∨"]
list_logicSymbol = ["¬", "→"]

def infix_to_postfix(expression):
    precedence = {"¬": 3, "∧": 2, "∨": 1}
    stack = []
    postfix = []
    for token in expression:
        if token in precedence:  # token이 연산자인 경우
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                postfix.append(stack.pop())
            stack.append(token)
        else:  # token이 피연산자인 경우
            postfix.append(token)

    while stack:
        postfix.append(stack.pop())

    return postfix

def postfix_to_infix(expression):
    stack = []
    for token in expression:
        if token in ["∧", "∨"]:  # token이 이항 연산자인 경우
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"({operand1} {token} {operand2})")
        elif token == "¬":  # token이 단항 연산자인 경우
            operand = stack.pop()
            stack.append(f"¬{operand}")
        else:  # token이 피연산자인 경우
            stack.append(token)

    return stack[0]





def stringToList(String):
    return [part.strip() for part in String.split()]


# coffee를 a로 간단화하는 과정, 입력 expression은 list임
def Translation(expression,dic):
    expression = infix_to_postfix(expression) # 후위표현법
    expression = convert(expression)
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

def convert_left(expression):
    ch1 = 97  # 'a' in ASCII
    ch2 = 97  # 'a' in ASCII
    dictionary = {}

    for i, token in enumerate(expression):
        if token in list_logicOperator:
            continue
        if token.startswith("¬"):
            token = token[1:]
            negation = True
        else:
            negation = False

        if token not in dictionary:
            dictionary[token] = chr(ch1)
            ch1 += 1

        ch2_temp = chr(ch2)
        ch2 += 1
        if ch2 > 122:  # 'z' in ASCII
            ch2 = 97  # reset to 'a'

        replacement = dictionary[token] + ch2_temp
        if negation:
            replacement = "¬" + replacement
        expression[i] = replacement

    return expression


def convert_right(expression, dic, idx):
    ch = max([ord(key[0]) for key in dic.keys()]) + 1
    for i, value in enumerate(expression):
        if value == list_logicOperator[0] or value == list_logicOperator[1]:
            continue
        if value.startswith("¬"):
            value = value[1:]
        if value not in dic:
            dic[value] = []
            idx[value] = 0
            ch += 1
        dic[value].append(chr(ch) + chr(97 + len(dic[value])))
    for i, value in enumerate(expression):
        if value.startswith("¬"):
            value = value[1:]
        if value in dic:
            if expression[i].startswith("¬"):
                expression[i] = "¬" + dic[value][idx[value]]
            else:
                expression[i] = dic[value][idx[value]]
            idx[value] += 1
    return expression, dic

# Main
inputString = "coffee ∧ coffee ∨ ¬tea → latte ∨ coffee ∧ tea"

logics = inputString.split("→")
leftLogic = stringToList(logics[0])
rightLogic = stringToList(logics[1])

leftLogic, dic, idx = convert_left(leftLogic)
leftLogic = infix_to_postfix(leftLogic)
leftLogic = postfix_to_infix(leftLogic)

rightLogic, dic = convert_right(rightLogic, dic, idx)
rightLogic = infix_to_postfix(rightLogic)
rightLogic = postfix_to_infix(rightLogic)

completely_expression = leftLogic + " → " + rightLogic
print(completely_expression)







