N,M=map(int,input().split())
lst=list(map(int,input().split()))
res=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if lst[i]+lst[j]+lst[k]>M:
                continue
            else:
                res=max(res,lst[i]+lst[j]+lst[k])
print(res)