wb = ['WBWBWBWB','BWBWBWBW']*4
bw = ['BWBWBWBW','WBWBWBWB']*4

N,M=map(int,input().split())
cnt_wb,cnt_bw=0,0
for i in range(N):
    lst=list(input())
    cnt_wb=[i for i in wb[i]]
