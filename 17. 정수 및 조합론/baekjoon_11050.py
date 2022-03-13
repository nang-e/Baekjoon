n,k=map(int,input().split())
def f(n):
  m,i=1,1
  while i<=n:
    m*=i ; i+=1
  return m
print(int(f(n)/(f(k)*f(n-k))))