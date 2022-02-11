A = int(input())
B = int(input())
C = int(input())
k = str(A*B*C)
for i in range(10):
    print(k.count(f'{i}'))
