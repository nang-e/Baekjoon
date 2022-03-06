n,m=map(int,input().split())
def euclidean(n,m):
    if n<m: n,m=m,n
    while m!=0:
        n,m=m,n%m
    return n
gcf=euclidean(n,m)
print(gcf,int(n*m/gcf),end='\n')