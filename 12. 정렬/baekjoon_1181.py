import sys
s=sys.stdin.readline

n=int(s())
lst=list(set(s().strip() for _ in range(n)))

lst.sort()
lst.sort(key=lambda x: len(x))

for i in lst:
  print(i)