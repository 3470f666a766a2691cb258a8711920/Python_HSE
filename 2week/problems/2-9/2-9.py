N = int(input())
if 11 <= N <= 19:
    print(N, 'korov')
elif (4 < N % 10 <= 9) or (N % 10 == 0):
    print(N, 'korov')
elif (N % 10 == 1):
    print(N, 'korova')
else:
    print(N, 'korovy')
