def divided_sum(n):
    return sum(map(int,list(str(n))))+n
N=int(input())
i=int(N/2)
while True:
    if N==divided_sum(i):
        print(i)
        break
    elif N==i:
        print(0)
        break
    else:
        i+=1