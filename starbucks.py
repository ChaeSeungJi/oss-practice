from itertools import product

# 고객이 주문한 음료수 리스트를 저장하는 리스트
order_list = []

# 고객이 주문한 음료수를 입력받아 order_list에 추가하는 함수


def add_order():
    menu = ['coffee', 'tea', 'latte', 'milk']
    while True:
        order_input = input("음료수를 입력하세요: ")
        orders = order_input.split(' and ') if 'and' in order_input else order_input.split(' or ')
        for order in orders:
            if order not in menu:
                print("잘못된 입력입니다.")
                break
            order_list.append((order, 1))
        more = input("계속 주문하시겠습니까? (Y/N) ")
        if more == 'N':
            break



# 가능한 모든 조합을 계산하는 함수
def calculate_combinations(order_list):
    combinations = []
    for combination in product([0, 1], repeat=len(order_list)):
        temps = []
        for i, order in enumerate(order_list):
            temps.append((order[0], combination[i]))
        i = 0
        while True:
            if temps[i][1] != 0:
                combinations.append(temps)
                break
            if (i == len(temps)-1):
                break
            i+=1

    return combinations

# 가능한 모든 조합을 출력하는 함수


# 가능한 모든 조합을 출력하는 함수
def print_combinations(combinations):
    for combination in combinations:
        print(combination)


# 음료수 주문을 입력받아 가능한 모든 조합을 출력합니다.
add_order()
combinations = calculate_combinations(order_list)
print_combinations(combinations)



# To do list
# 1. and일 때의 처리
# 2. 정해지지 않은 문자열 처리
# 3. 복잡한 논리식의 처리
