N = int(input())
def factorization(N):
    v = 2
    while N != 1:
        if N % v ==0:
            N /= v
            print(v)
        else:
            v += 1
factorization(N)