n=int(input())
lst,i=[],1
for _ in range(n):
  lst.append(input())
while 1:
  if len(set(map(lambda x: x[-i:],lst)))==len(lst):
    break
  i+=1
print(i)