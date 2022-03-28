import sys
n,m=map(int,sys.stdin.readline().split())
n_hear=[sys.stdin.readline().strip() for _ in range(n)]
n_see=[sys.stdin.readline().strip() for _ in range(m)]
lst=list(set(n_hear)&set(n_see))
lst.sort()
print(len(lst),*lst, sep='\n')