# 내가 쓴 코드
N = input()
if (N=='1')|(N=='2')|(N=='4')|(N=='7'):
    print(-1)
else:
    if N[-1] in ['0','3','5','8']:
        cnt_5 = int(N)//5
    elif N[-1] in ['1','4','6','9']:
        cnt_5 = int(N)//5-1
    elif N[-1] in ['2','7']:
        cnt_5 = int(N)//5-2
    cnt_3 = (int(N)-5*cnt_5)//3
    print(cnt_5+cnt_3)

# 다른 분이 쓰신 좋아보이는 코드
N = int(input())

answer = 0

while N >= 0:
    if N % 5 == 0 :
        print(N//5 + answer)
        break
    N -=3
    answer+=1
else:
    print(-1)