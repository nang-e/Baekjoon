T = int(input())
for t in range(T):
    R, S = input().split()
    k = ''
    for i in list(S):
        k += i*int(R)
    print(k, end='\n')
