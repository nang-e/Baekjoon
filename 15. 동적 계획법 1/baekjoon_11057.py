n=int(input())

d=[[0 for col in range(10)] for row in range(1001)]
d[0]=[1,1,1,1,1,1,1,1,1,1]

for i in range(1,n):
    for j in range(10):
        d[i][j]=(sum(d[i-1][:j+1]))%10007
print(sum(d[n-1])%10007)