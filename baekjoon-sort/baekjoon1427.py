import sys
input = sys.stdin.readline().rstrip()
number = input

num_list = list(map(str,str(number)))

num_list.sort(reverse=True)

str_num = ""

for i in num_list:
    str_num+=i

print(str_num)
