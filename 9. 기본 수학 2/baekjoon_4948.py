# 시간초과 당해버린 코드
# 1. n이 소수인지 판단하는 코드
def prime(n):
    i=2
    while i*i<=n:
        if not n%i:
            return False
        else:
            i+=1
    return True if n!=1 else False

# 2. n초과 2n이하의 숫자 중 소수의 개수를 세는 코드
def prime_cnt(n):
    cnt=0
    for i in range(n+1,2*n+1):
        if prime(i):
            cnt+=1
    return cnt

# 3. 1,2번의 코드를 결합하여 들어오는 숫자들마다 소수의 개수를 count하는 코드
while True:
    n=int(input())
    if n:
        print(prime_cnt(n))
    else:
        break

# 통과한 내코드
def prime(n):
    seive=[True]*n
    for i in range(2,int(n**1/2)+1):
        if seive[i]:
            for j in range(i*i,n,i):
                seive[j]=False
    return [i for i in range(2,n) if seive[i]]

def count(n):
    return len(set(prime(n*2+1))-set(prime(n+1)))

while True:
    n=int(input())
    if not n:
        break
    else:
        print(count(n))

# 개빠른 남의 코드
import sys
input = sys.stdin.readline

check = [0] * 2 + [1] * 246912

#첫 소수만 1로 남기고
#소수의 배수들은 소수가 아니므로 0으로 초기화
for i in range(2, 246913):
    if check[i]:
        for j in range(i * 2, 246913, i):
            check[j] = 0

while True:
    x = int(input())
    if x == 0:
        break
    print(sum(check[x+1:x*2+1]))