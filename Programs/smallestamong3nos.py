a = int(input("Enter 3 numbers:"))
b = int(input())
c = int(input())
if a < b:
    if a < c:
        print(a, "is smallest number")
    else:
        print(c, "is smallest number")
else:
    if b < c:
        print(b, "is smallest number")
    else:
        print(c, "is smallest number")
