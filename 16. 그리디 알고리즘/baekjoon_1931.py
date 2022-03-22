import sys
s=sys.stdin.readline
n=int(s())
lst=[[0,0] for _ in range(n)]

for i in range(n):
  lst[i][0],lst[i][1]=map(int,s().split())
lst.sort(key=lambda x: (x[0]))
lst.sort(key=lambda x: (x[1]))

end=lst[0][1]
cnt=1
for i in range(1,n):
  if lst[i][0]>=end:
    cnt+=1
    end=lst[i][1]
print(cnt)