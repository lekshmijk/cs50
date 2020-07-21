from cs50 import get_int

h = 0
while (h < 1 or h > 8):
    h = get_int("Please enter a height:")

for i in range (1,h+1):
    print(" " * (h-i), end = "")
    print("#" * i, end = "")
    print(" ", end = "")
    print("#" * i)
