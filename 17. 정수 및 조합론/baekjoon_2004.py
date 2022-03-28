def f(n):
  ans=1
  if n<=1:
    return ans
  else:
    for i in range(2,n+1):
      ans*=i
  return ans

n,m=map(int,input().split())
res=f(n)/(f(m)*f(n-m))

if res==int(res):
  res=int(res)
  idx=0
  while 1:
    idx+=1
    if str(res)[-idx]!='0':
      print(idx-1)
      break
else:
  print(0)