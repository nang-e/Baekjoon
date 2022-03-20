# 시간초과 ㅠ.ㅠ
def desc(k):
  s=str(k)
  for i in range(len(s)-1):
    if s[i]<=s[i+1]:
      return False
  return True

n=int(input())
if n>8003:
  print(-1)
else:
  cnt,i=0,0
  while cnt<n:
    if desc(i): cnt+=1
    i+=1
  print(i)