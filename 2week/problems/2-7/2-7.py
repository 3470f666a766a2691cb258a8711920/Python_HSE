h1 = int(input())
w1 = int(input())
h2 = int(input())
w2 = int(input())

if (h1 + w1) % 2 == (h2 + w2) % 2:
    print("YES")
else:
    print("NO")
