a = int(input())
yr = 1 if ((a%4==0)&(a%100!=0))|(a%400==0) else 0
print(yr)
