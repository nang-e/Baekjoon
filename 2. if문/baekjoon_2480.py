import sys
N = list(map(int, sys.stdin.readline().split()))
l = len(set(N))
if l == 1:
    print(10000+N[0]*1000)
elif l == 3:
    print(max(N)*100)
else:
    print(1000+[i for i in N if N.count(i) == 2][0]*100)
