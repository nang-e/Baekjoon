import sys
s=sys.stdin.readline
lst=[0]*10001
n=int(s())
for _ in range(n):
    num = int(s())
    lst[num] += 1
    
for i in range(10001):
    if lst[i]:
        for _ in range(lst[i]):
            print(i)