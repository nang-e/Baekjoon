def group_str(words):
    idx=0
    while idx<=(len(words)-2):
        if (len(words)==1)|(len(words)==2):
            return True
        elif (words[idx]!=words[idx+1])&(words.find(words[idx],idx+2)!=-1):
            return False
        else:
            idx+=1
    return True

T,cnt=int(input()),0
for _ in range(T):
    words=input()
    if group_str(words): cnt+=1
print(cnt)