import sys
n=int(input())
def mul(dic):
    i,val=1,dic.values()
    if len(dic.keys())==1:
        return list(val)[0]
    else:
        for v in val:
            i*=(v+1)
        return i-1
    
for i in range(n):
    dic={}
    case=int(input())
    if not case: print(0) ;continue
    for c in range(case):
        n,k= sys.stdin.readline().split()
        if k in dic.keys(): dic[k]+=1
        else:
            dic[k]=1
    print(mul(dic))