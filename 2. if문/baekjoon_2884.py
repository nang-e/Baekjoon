H,M = input().split()
H,M = int(H),int(M)

if M < 45:
    H -= 1
    M += 15
else:
    M -= 45

H = 24+H if (H<0) else H

print(H, M, end=' ')
