hours1 = int(input())
minutes1 = int(input())
secundes1 = int(input())

hours2 = int(input())
minutes2 = int(input())
secundes2 = int(input())

# hours1 = 1
# minutes1 = 1
# secundes1 = 1

# hours2 = 2
# minutes2 = 2
# secundes2 = 2

N = 3600 * hours2 + 60 * minutes2 + secundes2 -\
    3600 * hours1 - 60 * minutes1 - secundes1
print(N)
