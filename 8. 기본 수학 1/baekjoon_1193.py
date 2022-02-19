N = int(input())

def seq(n):
    return n**2/2-n/2+1
    
cnt = 1
while N >= seq(cnt):
    cnt += 1
c = cnt - 1
A = int(N-seq(c)+1)
B = int(c-N+seq(c))
print((f'{A}/{B}') if (c)%2 == 0 else (f'{B}/{A}'))