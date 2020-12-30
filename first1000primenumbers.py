import math

i=2
flag=0
counter=0
j=3
print("first 1000 prime numbers are:\n")
while counter < 1000:
    while i <= math.sqrt(j):
        if j%i == 0:
            flag = 1
            break
        i += 1
    if flag == 0:
        print(j)
        counter += 1
    j += 1
    i = 2
    flag = 0
