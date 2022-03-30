n=int(input())
lst=[int(input()) for _ in range(n)]
ans=[]
for i in range(2,min(lst)*2):
  if len(set(map(lambda x:x%i, lst)))==1:
    ans.append(i)
print(*ans)