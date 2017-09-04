import sys
input = sys.stdin
maxElem = int(input.readline())
x = maxElem
if maxElem != 0:
    while(x != 0):
        if x > maxElem:
            maxElem = x
        x = int(input.readline())
print(maxElem)
