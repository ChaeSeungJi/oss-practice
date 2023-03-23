n,k=map(int,input().split())
score_list=list(map(int,input().split()))

score_list.sort()

print(score_list[n-k])

#글자하나 바꾸깅