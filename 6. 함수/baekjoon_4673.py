def sumAll(x):
    sum = 0
    while(x != 0):
        sum += x % 10
        x //= 10
    return sum


n = range(10000)
lst = sorted(set(n) - set(list(map(lambda x: x+sumAll(x), n))))
for _ in lst:
    print(_)
