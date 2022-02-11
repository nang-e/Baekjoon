N = input()
t, li = 0, [N]
while True:
    t += 1
    if int(N) < 10:
        a = '0'+N
        N = str(int(a[-1])*10 + int(N))
        li.append(N)
        if int(li[0]) == int(li[-1]):
            break
    else:
        N = str(N[-1]) + str(int(N[0])+int(N[-1]))[-1]
        li.append(N)
        if int(li[0]) == int(li[-1]):
            break
print(t)
