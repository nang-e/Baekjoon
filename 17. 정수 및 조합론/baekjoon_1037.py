# 낭니 방법
n = input()
divisor = sorted(list(map(int,input().split())))
print(divisor[0]*divisor[-1])

# 내가 본 현명한 방법
n = input()
divisor = list(map(int,input().split()))
print(min(divisor)*max(divisor))
