def pos(x1,y1,r1,x2,y2,r2):
    d=((x2-x1)**2+(y2-y1)**2)**(1/2)
    sum_r,diff_r=r1+r2,max(r1,r2)-min(r1,r2)
    if (x1==x2)&(y1==y2)&(r1==r2):
        print(-1)
    else:
        print(0 if d>sum_r else 1 if d==sum_r else 2 if (d<sum_r)&(d>diff_r) else 1 if d==diff_r else 0)

for _ in range(int(input())):
    nums=map(float,input().split())
    pos(*nums)
