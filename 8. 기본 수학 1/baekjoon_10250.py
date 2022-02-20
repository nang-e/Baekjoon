import sys
T = int(input())
for i in range(T):
    H,W,N = map(int,sys.stdin.readline().split())
    print(str(H)+format(N//H,'02') if N % H == 0 else str(N%H)+format(N//H+1,'02'))