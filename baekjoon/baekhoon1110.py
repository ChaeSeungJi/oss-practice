count = 0
for i in range(8):
    line = input()
    if (i % 2 == 0):   # 0,2,4,6
        for index, value in enumerate(line):
            if (index % 2 == 0) and (value == 'F'):
                count += 1
    else:
        for index, value in enumerate(line):
            if (index % 2 != 0) and (value == 'F'):
                count += 1

print(count)
