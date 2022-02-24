def read():
    return map(int,input().split())
x1,y1=read()
x2,y2=read()
x3,y3=read()
print(x3 if x1==x2 else x2 if x1==x3 else x1, y3 if y1==y2 else y2 if y1==y3 else y1)