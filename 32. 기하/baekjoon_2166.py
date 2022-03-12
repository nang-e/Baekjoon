n=int(input())
x,y=[],[]
for _ in range(n):
  xn,yn=map(int,input().split())
  x.append(xn);y.append(yn)
x.append(x[0]);y.append(y[0])
x_sum,y_sum=0,0
for i in range(n):
  x_sum+=x[i]*y[i+1]
  y_sum+=y[i]*x[i+1]
print(round(abs((x_sum-y_sum))/2,1))