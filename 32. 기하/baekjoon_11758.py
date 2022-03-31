x,y=[0,0,0,0],[0,0,0,0]
x[0],y[0]=map(int,input().split())
x[1],y[1]=map(int,input().split())
x[2],y[2]=map(int,input().split())
x[3],y[3]=x[0],y[0]
cp=(x[0]*y[1]+x[1]*y[2]+x[2]*y[3])-(x[1]*y[0]+x[2]*y[1]+x[3]*y[2])
print(0 if not cp else 1 if cp>0 else -1)