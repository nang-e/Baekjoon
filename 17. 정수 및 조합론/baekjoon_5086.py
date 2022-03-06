import sys
def judge(a,b):
    print('factor' if not b%a else 'multiple' if not a%b else 'neither')

while 1:
    a,b=map(int,sys.stdin.readline().split())
    if a==b:
        break
    elif (not a)|(not b):
        print('neither')
        pass
    else:
        judge(a,b)