import sys
s=sys.stdin.readline
n=int(s())
lst=[]
for _ in range(n):
  i=s().split()
  cmd=i[0]
  l=len(lst)
  if cmd=='push': lst.append(int(i[1]))
  elif cmd=='top': print(lst[-1] if l else -1)
  elif cmd=='empty': print(0 if l else 1)
  elif cmd=='size': print(l)
  else: print(lst.pop(-1) if l else -1)
