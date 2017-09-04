a = int(input())
b = int(input())
c = int(input())
if (a % 2 == 0):
    if (b % 2 == 1):
        print("YES")
    else:
        if(c % 2 == 1):
            print("YES")
        else:
            print("NO")

else:
    if(b % 2 == 0):
        print("YES")
    else:
        if (c %2 == 0):
            print("YES")
        else:
            print("NO")
