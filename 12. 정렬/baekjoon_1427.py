lst,ans=[0]*10,''
for i in input(): 
    lst[int(i)]+=1
for idx in range(9,-1,-1):
    if lst[idx]!=0:
        for _ in range(lst[idx]):
            ans+=str(idx)
print(int(ans))