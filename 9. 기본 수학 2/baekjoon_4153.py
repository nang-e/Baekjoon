import sys
while True:
    a,b,c = sorted(map(int,sys.stdin.readline().split()))
    if (a==b)& (b==c):
        break
    elif c**2 == a**2+b**2:
        print('right')
    else:
        print('wrong')