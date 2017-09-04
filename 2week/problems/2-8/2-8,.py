N = int(input())
M = int(input())
K = int(input())

if ((K % M == 0) or (K % N == 0)) and (K < M * N):
    print("YES")
else:
    print("NO")
