C = int(input())
for _ in range(C):
    test = list(map(int, input().split()))
    n, lst = test[0], test[1:]
    avg = sum(lst)/n
    per = len(list(filter(lambda x: x > avg, lst)))/n*100
    print(format(per, '.3f')+"%")
