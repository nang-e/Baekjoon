n=int(input())
for _ in range(n):
    s=input()
    l=len(s)
    if l%2: print('NO')
    else: 
        while '()' in s:
            s=s.replace('()','')
        if not s: print("YES")
        else: print('NO')