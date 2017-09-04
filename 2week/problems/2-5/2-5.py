h1 = int(input())
w1 = int(input())
h2 = int(input())
w2 = int(input())
if abs(h1 - h2) <= 1 and abs(w1 - w2) <= 1:
    print("YES")
else:
    print("NO")
