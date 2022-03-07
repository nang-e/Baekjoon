# 내장함수 sorted 사용
import sys
lst=[]
for _ in range(int(input())):
    lst.append(int(sys.stdin.readline()))
print(*sorted(lst), end='\n')

# 버블정렬 - 시간복잡도 O(n^2)
lst=[]
for _ in range(int(input())):
    lst.append(int(input()))

def bubblesort(lst):
    while 1:
        changed=0
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                changed=1
        if not changed:
            return lst
print(*bubblesort(lst),end='\n')
