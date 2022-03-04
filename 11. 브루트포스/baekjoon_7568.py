N=int(input())
lst=[]
for _ in range(N):
    x,y=map(int,input().split())
    lst.append([x,y])

cnts=[]
for i in range(N):
    cnt=1
    for j in range(N):
        if (lst[j][0]>lst[i][0]) & (lst[j][1]>lst[i][1]):
            cnt+=1
    cnts.append(cnt)
print(*cnts)