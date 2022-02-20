import sys
T = int(sys.stdin.readline())
for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    cnt, denominator, numerator = 1,1,n
    while k >= cnt:
        denominator *= (cnt+1)
        numerator *= (n+cnt)
        cnt += 1
    print(int(numerator/denominator))