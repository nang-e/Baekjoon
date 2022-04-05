word=input()
s=input()
l=len(s)
cnt=0
while 1:
  if word.find(s)==-1:
    break
  idx=word.find(s)
  cnt+=1
  word=word[idx+l:]
print(cnt)