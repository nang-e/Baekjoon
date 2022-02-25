def prime(n):
    seive=[True]*n
    for i in range(2,int(n**1/2)+1):
        if seive[i]:
            for j in range(i*i,n,i):
                seive[j]=False
    return [i for i in range(2,n) if seive[i]]

M,N=int(input()),int(input())
prime_set=set(prime(N+1))-set(prime(M))
if sum(prime_set):
    print(sum(prime_set),min(prime_set),end='\n')
else:
    print(-1)