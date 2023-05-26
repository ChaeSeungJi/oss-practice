import re
import copy

class starbucks2:

    def __init__(self) -> None:
        pass

    list_logicOperator = ["∧", "∨"]
    list_logicSymbol = ["¬", "→"]

    # 후위표현법으로 변환
    def infix_to_postfix(self,expression):
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


    def postfix_to_infix(self,expression):
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

    def convert_left(self,expression, dic):
        ch = 97
        dic2 = {}
        for v in dic:
            list = []
            ch2 = 97
            for i in range(dic[v]):
                list.append(chr(ch)+chr(ch2))
                ch2 += 1
            dic2[v] = list
            ch += 1
        dic2_out = copy.deepcopy(dic2)
        idx = 0
        for i, v in enumerate(expression):
            if v == self.list_logicOperator[0] or v == self.list_logicOperator[1]:
                continue
            if v.startswith("¬"):
                key = v[1:]
                if key in dic2:
                    expression[i] = "¬" + dic2[key].pop(0)
            elif v in dic2:
                expression[i] = dic2[v].pop(0)
        return expression, dic2_out, ch


    def convert_right(self,expression, dic, ch):  # list,dictionary
        dic_new = {}  # key : "aa" value: [ch1,ch2]
        dic_copy = copy.deepcopy(dic)
        ch2 = 97
        for i, v in enumerate(expression):
            if v == self.list_logicOperator[0] or v == self.list_logicOperator[1]:
                continue
            if v.startswith("¬"): # not 연산일 때
                key = v[1:]
                if key in dic:
                    expression[i] = "¬" + dic[key].pop(0)
                else:
                    if key not in dic_new:
                        dic_new[key] = [ch, ch2]
                        expression[i] = "¬" + \
                            chr(dic_new[key][0])+chr(dic_new[key][1])
                        ch + 1
                        dic_new[key][1] += 1
                    else:
                        dic_new[key] = (dic_new[key][0]+1, dic_new[key][1]+1)
                        expression[i] = "¬" + \
                            chr(dic_new[key][0])+chr(dic_new[key][1])
                        dic_new[key][1] += 1
            elif v in dic: # 기존 단어
                if len(dic[v]) != 0:
                    expression[i] = dic[v].pop(0)
                else:
                    s = dic_copy[v][-1]
                    first = s[0]
                    second = s[1]
                    code = ord(second) + 1
                    expression[i] = first + chr(code)

            else: # 새로운 단어
                if v not in dic_new:
                    dic_new[v] = [ch, ch2]
                    expression[i] = chr(dic_new[v][0])+chr(dic_new[v][1])
                    ch + 1
                    dic_new[v][1] += 1
                else:
                    dic_new[v] = (dic_new[v][0]+1, dic_new[v][1]+1)
                    expression[i] = chr(dic_new[v][0])+chr(dic_new[v][1])
                    dic_new[v][1] += 1

        return expression


    # 리스트에서 같은 문자열을 카운트해서 딕셔너리로 반환한다.
    def countOverlappingString(self,li: list):
        s1 = set(li)
        s1.discard("∧")
        s1.discard("∨")
        dic = {}
        for v in s1:
            if v.startswith("¬"):
                v = v[1:]
            dic[v] = 0
        for v in li:
            if v.startswith("¬"):
                v = v[1:]
            if v in dic:
                dic[v] += 1
        return dic


    def stringToList(self,String):
        return [part.strip() for part in String.split()]


    # coffee를 a로 간단화하는 과정, 입력 expression은 list임
    def Translation_left(self,expression, dic):
        expression = self.infix_to_postfix(expression)  # 후위표현법
        expression, dic_tmp, ch = self.convert_left(expression, dic)
        expression = self.postfix_to_infix(expression)  # 문자열 상태,중위표현법
        return expression, dic_tmp, ch


    def Translation_right(self,expression, dic, ch):
        expression = self.infix_to_postfix(expression)  # 후위표현법
        expression = self.convert_right(expression, dic, ch)
        expression = self.postfix_to_infix(expression)  # 문자열 상태,중위표현법
        return expression


    def main(self,inputString):
        # 여기서부터는 메인 내용
        # inputString = "coffee ∧ ¬coffee ∨ tea → coffee ∨ coffee ∨ coffee"
        logics = inputString.split("→")
        leftLogic = logics[0]
        leftLogic = self.stringToList(leftLogic)
        rightLogic = logics[1]
        rightLogic = self.stringToList(rightLogic)
        # ============= 좌 우 문자열로 이루어진 논리식을 공백을 구분자로 리스트로 만듦

        # 왼쪽 논리식을 변환하는 과정
        dicleft = self.countOverlappingString(leftLogic)
        leftLogic, dic_tmp, ch = self.Translation_left(leftLogic, dicleft)


        # 오른쪽 논리식을 변환하는 과정
        # dicright = countOverlappingString(rightLogic)
        rightLogic = self.Translation_right(rightLogic, dic_tmp, ch)


        completely_expression = leftLogic + " → " + rightLogic
        return completely_expression

