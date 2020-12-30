import math
i=2
flag=0
num=int(input("Enter a number:"))
while i <= math.sqrt(num):
    if num%i == 0:
        flag = 1
        break
    i+=1
if flag == 1:
    print(str(num)+" is not a prime number")
else:
    print(str(num)+" is a prime number")
