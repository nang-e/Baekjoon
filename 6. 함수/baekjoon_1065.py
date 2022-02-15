N = int(input())


def numCheck(i):
    l = len(str(i))
    sumSet = set(map(lambda x: int(str(i)[x]) - int(str(i)[x+1]), range(l-1)))
    return len(sumSet)


def seq(N):
    i, cnt = 1, 0
    while i <= N:
        if (i <= 99) | (numCheck(i) == 1):
            cnt += 1
        else:
            pass
        i += 1
    return cnt


print(seq(N))
