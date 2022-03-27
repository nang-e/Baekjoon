import sys
s=sys.stdin.readline
n=int(s())
arr=list(map(int,s().split()))
arr2=sorted(set(arr))

dic={v:i for i,v in enumerate(arr2)}
for i in arr:
  print(dic[i], end=' ')