import sys
N=int(sys.stdin.readline())
p_i=sorted(list(map(int,sys.stdin.readline().split())))
s=0
for i in range(N):
  s+=sum(p_i[:(i+1)])
print(s)