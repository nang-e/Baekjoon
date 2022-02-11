import sys
T = int(input())
for i in range(T):
    n1,n2 = map(int,sys.stdin.readline().split())
    print(f'Case #{i+1}: {(n1+n2)}')
