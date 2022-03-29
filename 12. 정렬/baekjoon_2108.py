from collections import Counter as c
import sys

s=sys.stdin.readline
n=int(s())
lst=[int(s()) for _ in range(n)] ; lst.sort()
def mode(lst):
    m=c(lst).most_common()
    if (len(m)>1):
        if (m[0][1]==m[1][1]):
            return m[1][0]
    return m[0][0]
q1=round(sum(lst)/n)
q2=lst[int((n+1)/2)-1]
q3=mode(lst)
q4=lst[-1]-lst[0]
print(q1,q2,q3,q4,sep='\n')