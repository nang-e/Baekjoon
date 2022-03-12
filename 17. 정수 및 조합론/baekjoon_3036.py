n=int(input())
ring=list(map(int,input().split()))
st=ring[0]
def gcf(m,n):
  if m<n: m,n=n,m
  while n>0:
    m,n=n,m%n
  return m
for i in range(1,n):
  print(int(st/gcf(st,ring[i])),'/',int(ring[i]/gcf(st,ring[i])),sep='')