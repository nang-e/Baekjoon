import sys
def f(n):
    return 0 if n==0 else 1 if n==1 else f(n-1)+f(n-2)
f(int(sys.stdin.readline()))