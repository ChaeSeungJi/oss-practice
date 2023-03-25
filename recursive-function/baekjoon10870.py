global rec_count
rec_count =0
def recursive(s, l, r):
    global rec_count 
    rec_count += 1
    if l>=r : 
        t = (1,rec_count)
        rec_count =0
        return t
    elif s[l] != s[r]:
        t = (0,rec_count)
        rec_count =0
        return t
    else:
        return recursive(s, l+1, r-1)

def isPalaindrome(s):
    return recursive(s, 0, len(s)-1)

N = (int)(input())
list_s = []

for i in range(N):
    list_s.append(isPalaindrome(input()))
    print(*list_s[i])



