s=input().split('-')
c=int(sum(map(int,s[0].split('+'))))
if len(s):
  for i in range(1,len(s)):
    c-=sum(map(int,s[i].split('+')))
print(c)