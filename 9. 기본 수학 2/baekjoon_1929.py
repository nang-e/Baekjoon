def prime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            cnt=1
            break
        

        i+=1
