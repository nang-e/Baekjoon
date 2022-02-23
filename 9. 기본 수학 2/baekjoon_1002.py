T=int(input())

def pos(x1,y1,r1,x2,y2,r2):
    d=float((x2-x1)**2+(y2-y1)**2)
    d_r=float((r1+r2)**2)
    if (x1==x2)&(y1==y2)&(r1==r2):
        print(-1)
    elif (x1==x2)&(y1==y2)&(r1!=r2):
        print(0)
    else:
        print(1 if d==d_r else 2 if d<=d_r else 0)

for _ in range(T):
    nums=map(int,input().split())
    pos(*nums)

