def draw_pattern(n):
    if n == 1:
        return ['*']
    else:
        # 크기 n/3의 패턴을 그립니다.
        pattern = draw_pattern(n // 3)
        # 크기 n의 패턴을 그립니다.
        result = []
        for line in pattern:
            result.append(line * 3)
        for line in pattern:
            result.append(line + ' ' * (n // 3) + line)
        for line in pattern:
            result.append(line * 3)
        return result
    

def draw_star_pattern(n):
    pattern = draw_pattern(n)
    for line in pattern:
        print(line)

n = (int)(input())

draw_star_pattern(n)