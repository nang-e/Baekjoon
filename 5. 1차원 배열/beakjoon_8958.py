import sys
n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().strip().split('X')
    case = list(filter(None, line))
    print(sum(list(map(lambda x: int((1+len(x))/2*len(x)), case))))
