def prime(n):
    i=2
    while i*i<=n:
        if not (n%i):
            return False
        else:
            i+=1
    return True if n!=1 else False

T=int(input())
nums=map(int,input().split())
cnt=0
for num in nums:
    if prime(num):
        cnt+=1
print(cnt)