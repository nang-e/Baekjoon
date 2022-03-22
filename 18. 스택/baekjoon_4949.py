import re,sys
while 1:
  i=sys.stdin.readline().rstrip()
  if i=='.':
    break
  i=re.sub('[ a-zA-Z.]','',i)
  while 1:
    i=i.replace('()','').replace('[]','')
    if ('()' not in i) & ('[]' not in i):
      break
  print('no' if len(i) else 'yes')