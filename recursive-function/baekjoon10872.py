def recursive(n):
    if n==0: return 1
    elif n==1: return n
    else:
        return n*recursive(n-1)
    

N = (int)(input())

print(recursive(N))