N = int(input())

def seq(n):
    return 3*n**2-3*n+2

n = 1
if N == 1:
    print(1)
else:
    while True:
        if N in range(seq(n), seq(n+1)):
            print(n+1)
            break
        else:
            n += 1

# 시간 단축 코드
N = int(input())

def seq(n):
    return 3*n**2-3*n+2

n = 1
if N == 1:
    print(1)
else:
    while N >= seq(n):
        n += 1
    print(n)
