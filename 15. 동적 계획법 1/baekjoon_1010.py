import sys
s=sys.stdin.readline
for _ in range(int(s())):
    n,m=map(int,s().split())
    d=[[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if (i==j)|(j==0): d[i][j]=1
            else: d[i][j]=d[i-1][j]+d[i-1][j-1]

    print(d[m][n])