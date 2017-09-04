import math
H = int(input())
A = int(input())
B = int(input())
print(math.ceil((H - A) / (A - B)) + 1)
