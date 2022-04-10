n,m=map(int,input().split())
d=[i for i in range(101)]
for i in range(2,101):
  d[i]*=d[i-1]
print(d[n]//(d[m]*d[n-m]))