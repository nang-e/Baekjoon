from numpy import average


N = int(input())
currentScore = list(map(int, input().split()))
M, lst = max(currentScore), []
for s in currentScore:
    lst.append(s/M*100)
print(sum(lst)/len(lst))
