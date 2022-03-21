a,b,c=map(int,input().split())
ans=1
for _ in range(b):
  ans=ans*a%c
print(ans)