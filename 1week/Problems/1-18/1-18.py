N = int(input())
print('{0:01d}:{1:02d}:{2:02d}'.format(N // 3600 % 24, N // 60 % 60, N % 60))
