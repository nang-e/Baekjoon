def prime(n):
    i=2
    cnt=0
    while i*i<=n:
        if n%i==0:
            cnt=1
            break
        i+=1
    return cnt