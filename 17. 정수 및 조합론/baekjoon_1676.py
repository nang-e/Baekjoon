n=int(input())
idx,res=0,1
if not n:
    res=1
else:
    for i in range(1,n+1):
        res*=i    

while 1:
    idx+=1
    if str(res)[-idx]!='0':
        print(idx-1)
        break