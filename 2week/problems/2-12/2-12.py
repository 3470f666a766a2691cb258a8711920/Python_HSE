x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (1 <= x1 <= 8) and (1 <= y1 <= 8):
    if ((x1 + y1) % 2 == 0) and ((x2 + y2) % 2 == 0):
        if (y2 >= x1 + y1 - x2) and (y2 >= x2 + y1 - x1) and (y2 > y1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
