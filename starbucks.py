import re


# logic_symbols = {"and": "∧", "or": "∨", "~": "¬", "$": "→"}
list_logicOperator = ["∧", "∨"]
list_logicSymbol = ["¬", "→"]




def splitLogic(logicString : list):
    # '|'는 정규 표현식에서 '또는'을 의미하며, re.escape는 논리 기호가 정규 표현식의 특수 문자가 아니라는 것을 보장합니다.
    parts = re.split('|'.join(map(re.escape, list_logicOperator)), leftLogic)
    # 각 부분에서 앞뒤 공백 제거
    parts = [part.strip() for part in parts]
    return parts

def makeOperatorIdx(operatorDic:dict,logic:list):
    order = 1
    for operator in list_logicOperator:
        index = logic.find(operator)
        if index != -1:  # 기호가 문자열에 있다면
            operatorDic[operator] = order
            order += 1




# logics = inputString.split("$")
# leftLogic = logics[0]
# rightLogic = logics[1]

# leftOperatordic = {}
# rightOperatordic = {}

# while 1:
#     start_and = leftLogic.find("and"); start_or=leftLogic.find("or")
#     end_and = 0; end_or=0
#     if (start_and== -1) and (start_or==-1):
#         break
#     else:

# ============= 주석 처리된 부분은 입력값이 논리기호가 아닌 문자열로 들어왔을 때 처리하려고 했으나 나중에 생각하기

inputString = "coffee ∧ coffee → coffee ∨ coffee"
logics = inputString.split("→")
leftLogic = logics[0]
rightLogic = logics[1]

leftOperator_order ={}
rightOperator_order ={}

print(leftLogic)
makeOperatorIdx(leftOperator_order,leftLogic)

# 논리 기호를 구분자로 문자열 분리
# '|'는 정규 표현식에서 '또는'을 의미하며, re.escape는 논리 기호가 정규 표현식의 특수 문자가 아니라는 것을 보장합니다.
parts = re.split('|'.join(map(re.escape, list_logicOperator)), leftLogic)
# 각 부분에서 앞뒤 공백 제거
parts = [part.strip() for part in parts]

outLeftLogic = ["_"] * len(parts)

print(leftOperator_order)

# setLeftLogic = set(parts)

# for i in range(len(parts)):






