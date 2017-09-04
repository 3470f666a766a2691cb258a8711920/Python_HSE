N = int(input())
S = 0
while N >= 2:
    if N % 2 == 1:
        S += 1
        break
    N = N // 2
if S:
    print("NO")
else:
    print("YES")
