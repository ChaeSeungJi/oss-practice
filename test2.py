dic = {"a":[1,2],"b":[3,4,5]}

if "b" in dic:
    dic["b"].pop(0)

print(*dic["b"])