import math

a = int(input("Enter coefficients of quadratic equation:"))
b = int(input())
c = int(input())
d = (b * b) - (4 * a * c)
if a==0:
    print("It is not a quadratic equation")
elif d >= 0:
    r1 = (-b + math.sqrt(d)) / 2
    r2 = (-b - math.sqrt(d)) / 2
else:
    rp = -b / 2
    ip = math.sqrt(-d) / (2 * a)
    r1 = complex(rp, ip)
    r2 = complex(rp, -ip)
print("roots of quadratic equations are:", r1, " & ", r2)
