n=int(input())
d={}
for _ in range(n):
  name=input()
  if name not in d: d[name]=1
  else: d[name]+=1
lst=list(d.items())
lst.sort(key=lambda x: (-x[1],x[0]))
print(lst[0][0])