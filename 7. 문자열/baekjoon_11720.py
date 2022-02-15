N = int(input())
num = input()
i, s = 0, 0
while i < N:
    s += int(num[i])
    i += 1
print(s)

# # 다른사람 풀이
# N = int(input())
# print(sum(list(map(int, input()))))
