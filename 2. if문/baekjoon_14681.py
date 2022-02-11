x = int(input())
y = int(input())
n = 1 if (x>0)&(y>0) else 2 if (x<0)&(y>0) else 3 if (x<0)&(y<0) else 4
print(n)
