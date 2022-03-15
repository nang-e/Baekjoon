# 내 풀이
import sys
bw,wb='BWBWBWBW','WBWBWBWB'
row=0
min_bw,min_wb=10000,10000
lst=[]
n,m=map(int,input().split())
for _ in range(n):
    lst.append(sys.stdin.readline())
while (row+8<=n):
    col=0
    while (col+8<=m):
        cnt_bw,cnt_wb=0,0
        brute_force=list(map(lambda x: lst[row:row+8][x][col:col+8],range(8)))
        for i in range(0,8,2):
            for j in range(8):
                if list(brute_force[i])[j]!=list(bw)[j]: cnt_bw+=1
                if list(brute_force[i+1])[j]!=list(wb)[j]: cnt_bw+=1
                if list(brute_force[i])[j]!=list(wb)[j]: cnt_wb+=1
                if list(brute_force[i+1])[j]!=list(bw)[j]: cnt_wb+=1
        min_bw,min_wb=min(min_bw,cnt_bw),min(min_wb,cnt_wb)
        col+=1
    row+=1
print(min(min_bw,min_wb))

# 다른 사람 풀이 1
def recolor(x, y):
    ans = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if 'BW'[(i+j)%2] != board[j][i]:
                ans+= 1
    return min(ans, 64-ans)

a, b = map(int,input().split())
board = [input() for i in range(a)]

ans = 64
for i in range(b-7):
    for j in range(a-7):
        ans = min(ans, recolor(i,j))
print(ans)

# 다른 사람 풀이 2
r=range
n,m=map(int,input().split())
board=[input() for i in r(n)]
a="WB"
t=[[(0,1)[a[(i+j)%2]==board[i][j]]for j in r(m)]for i in r(n)]
q=[[sum(t[i][j:j+8])for j in r(m-7)]for i in r(n)]
w=[sum(q[k+j][i]for j in r(8))for k in r(n-7)for i in r(m-7)]
print(min(64-max(w),min(w)))
