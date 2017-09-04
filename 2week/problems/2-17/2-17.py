A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

# A = 1
# B = 1
# C = 1
# D = 1
# E = 1

if (D >= A and E >= B) or (D >= B and E >= A) or\
    (D >= B and E >= C) or (D >= C and E >= B) or\
        (D >= C and E >= A) or (D >= A and E >= C):
    print("YES")
else:
    print("NO")
