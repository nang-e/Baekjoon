# 1.
while True:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except EOFError:
        break

# 2.
while True:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break

# 3.
import sys
lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int,line.split())
    print(A+B)
