import sys
def prime(n):
    lst=[True]*n
    for i in range(2,int(n**1/2)+1):
        if lst[i]:
            for j in range(i*i,n,i):
                lst[j]=False
    return [i for i in range(2,n) if lst[i]]

for _ in range(int(input())):
    n=int(input())
    lst=prime(n)
    if n/2 in lst:
        print(int(n/2),int(n/2))
    elif len(lst)%2:
        for k in range(int(len(lst)/2)+1,-1,-1):
            a,b=lst[k-1],n-lst[k-1]
            if (a in lst)&(b in lst):
                print(a,b)
                break
    else:
        for k in range(int(len(lst)/2),-1,-1):
            a,b=lst[k-1],n-lst[k-1]
            if (a in lst)&(b in lst):
                print(a,b)
                break

    # while i>=2:
    #     if prime(i)&prime(n-i):
    #         a,b=i,n-i
    #         break
    #     else:
    #         i-=1
    # print(a,b)