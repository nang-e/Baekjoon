def prime(n):
    i=2
    for i in range(2,n):
        if not n%i:
            return False
        else:
            i+=1
    return True if n!=1 else False

while True:
    cnt=0
    n=int(input())
    if not n:
        break
    for i in range(n+1,2*n+1):
        if prime(i):
            cnt+=1
    print(cnt)