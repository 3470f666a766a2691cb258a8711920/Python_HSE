A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())


# A1 = 1
# B1 = 2
# C1 = 3
# A2 = 3
# B2 = 2
# C2 = 1


if A1 > B1:
    A1, B1 = B1, A1
if A1 > C1:
    A1, C1 = C1, A1
if B1 > C1:
    B1, C1 = C1, B1

if A2 > B2:
    A2, B2 = B2, A2
if A2 > C2:
    A2, C2 = C2, A2
if B2 > C2:
    B2, C2 = C2, B2


if (A1 == A2) and (B1 == B2) and (C1 == C2):
    print("Boxes are equal")
elif (A1 <= A2) and (B1 <= B2) and (C1 <= C2) and\
        (A1 + B1 + C1 < A2 + B2 + C2):
            print("The first box is smaller than the second one")
elif (A1 >= A2) and (B1 >= B2) and (C1 >= C2) and\
        (A1 + B1 + C1 > A2 + B2 + C2):
            print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
