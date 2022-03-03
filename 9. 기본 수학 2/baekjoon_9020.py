def prime(n):
    lst=[True]*n
    for i in range(2,int(n**1/2)+1):
        if lst[i]:
            for j in range(i*i,n,i):
                lst[j]=False
    return [i for i in range(2,n) if lst[i]]

T=int(input())
for _ in range(T):
    n=int(input())
    lst=prime(n)
    idx=max([i for i in lst if i<=(n/2)])
    for k in range(idx,-1,-1):
        if (k in lst) & ((n-k) in lst):
            print(k,n-k)
            break