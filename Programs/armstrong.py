sum = 0
num = int(input("Enter a number:"))
que = num
while que != 0:
    rem = que % 10
    sum = sum + (rem * rem * rem)
    que = int(que / 10)
if sum == num:
    print(str(num) + " is an armstrong number")
else:
    print(str(num) + " is not an armstrong number")
