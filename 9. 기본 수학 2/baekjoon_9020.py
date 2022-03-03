# 최종
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

# 속도 개선
sieve=[1]*10001
sieve[0],sieve[1]=0,0
for i in range(2,101):
    if sieve[i]:
        for j in range(i*i,10001,i):
            sieve[j]=0

for _ in range(int(input())):
    n=int(input())
    a=n//2
    while 1:
        if sieve[a]&sieve[n-a]:
            print(a,n-a)
            break
        else:
            a-=1
