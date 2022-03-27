import syslog
t=sys.stdin.readline
n=int(t())
lst=[int(t()) for _ in range(n)] ; lst.sort()
s=sorted(set(lst))

def mode(lst):
  dic={}
  for i in s:
    dic[i]=lst.count(i)
  cnt=0
  for k,v in dic.items():
    if (list(dic.values()).count(max(dic.values()))>=2)&(v==max(dic.values())):
      cnt+=1
      if cnt==2:
        q3=k
        return q3
    elif (list(dic.values()).count(max(dic.values()))==1)&(v==max(dic.values())):
      q3=k
      return q3

q1=round(sum(lst)/n)
q2=lst[int((n+1)/2)-1]
q3=mode(lst)
q4=lst[-1]-lst[0]

print(q1,q2,q3,q4,sep='\n')