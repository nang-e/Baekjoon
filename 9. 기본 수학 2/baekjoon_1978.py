# 내코드 - 개선하기 !
import math
def prime(n):
    i,cnt = 2,0
    if n==1:
        cnt=-1
    else:
        while i<=math.sqrt(n):
            if i*i==n:
                cnt+=1
            elif n%i==0:
                cnt+=2
            i+=1
    return cnt

N = int(input())
k = list(map(int,input().split()))
cnt = 0
for i in range(N):
    if prime(k[i])==0:
        cnt+=1
print(cnt)

# 다른사람 풀이
# n = int(input())
# numbers = map(int, input().split())
# p = 0

# for num in numbers:
#     if num > 1:
#         i = 2
#         for i in range(2, num + 1):
#             if num % i == 0:
#                 break

#         if i == num:
#             p += 1

# print(p)