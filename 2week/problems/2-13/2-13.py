a = int(input())
b = int(input())
c = int(input())

max_side = max(a, b, c)
min_side = min(a, b, c)
middle_side = a + b + c - max_side - min_side
if min_side + middle_side <= max_side:
    print("impossible")
else:
    if (min_side ** 2 + middle_side ** 2 > max_side ** 2):
        print("acute")
    elif (min_side ** 2 + middle_side ** 2 < max_side ** 2):
        print("obtuse")
    else:
        print("rectangular")
