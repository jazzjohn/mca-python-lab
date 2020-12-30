digit = 0
num=int(input("Enter a number:"))
while num > 0:
    digit = digit+1
    num = int(num/10)
print('Number of digits in the entered number is: ' + str(digit))

