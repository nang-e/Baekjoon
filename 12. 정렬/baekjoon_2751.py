import sys
N=int(input())
lst=[int(sys.stdin.readline()) for i in range(N)]
lst.sort()
print(*lst,sep='\n')