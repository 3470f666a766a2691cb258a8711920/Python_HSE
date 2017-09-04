a = int(input())
b = int(input())
c = int(input())

# a = 1
# b = 2
# c = 3


if (a == b) and (a == c):
    count = 3
if (a == b) and (a != c):
    count = 2
if (a != b) and (a == c):
    count = 2
if (a != b) and (b == c):
    count = 2
if (a != b) and (b != c) and (a != c):
    count = 0
print(count)
