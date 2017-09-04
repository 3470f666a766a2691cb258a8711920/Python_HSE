a = int(input())
b = int(input())
c = int(input())
d = int(input())

# a = 2
# b = -4
# c = 7
# d = 1

if (a == 0) and (b == 0) and (c == 0) and (d == 0):
    print("NO")
if (a == 0) and (b == 0) and (c == 0) and (d != 0):
    print("INF")
if (a == 0) and (b == 0) and (c != 0) and (d == 0):
    print("INF")
if (a == 0) and (b == 0) and (c != 0) and (d != 0):
    print("INF")
if (a == 0) and (b != 0) and (c == 0) and (d == 0):
    print("NO")
if (a == 0) and (b != 0) and (c == 0) and (d != 0):
    print("NO")
if (a == 0) and (b != 0) and (c != 0) and (d == 0):
    print("NO")
if (a == 0) and (b != 0) and (c != 0) and (d != 0):
    print("NO")
if (a != 0) and (b == 0) and (c == 0) and (d == 0):
    print("NO")
if (a != 0) and (b == 0) and (c == 0) and (d != 0):
    print(0)
if (a != 0) and (b == 0) and (c != 0) and (d == 0):
    print("NO")
if (a != 0) and (b == 0) and (c != 0) and (d != 0):
    print(0)
if (a != 0) and (b != 0) and (c == 0) and (d == 0):
    print("NO")
if (a != 0) and (b != 0) and (c == 0) and (d != 0):
    if (b % a == 0):
        print(-b // a)
    else:
        print("NO")
if (a != 0) and (b != 0) and (c != 0) and (d == 0):
    if (b % a == 0):
        print(-b // a)
    else:
        print("NO")

if (a != 0) and (b != 0) and (c != 0) and (d != 0):
    if (b % a == 0):
        if(a * d == b * c):
            print("NO")
        else:
            print(-b // a)
    else:
        print("NO")
