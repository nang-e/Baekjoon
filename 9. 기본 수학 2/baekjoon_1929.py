def prime(n):
    seive=[True]*n
    for i in range(2,int(n**1/2)+1):
        if seive[i]:
            for j in range(i*i,n,i):
                seive[j]=False
    return [i for i in range(2,n) if seive[i]]

M,N=map(int,input().split())
prime_lst=list(set(prime(N+1))-set(prime(M)))
prime_lst.sort()
for i in prime_lst:
    print(i)