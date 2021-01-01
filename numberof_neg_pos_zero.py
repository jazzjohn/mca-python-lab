pos = 0
neg = 0
zero = 0
limit = int(input("Enter the limit:"))
print("Enter the values")
for i in range(1, limit + 1):
    num = int(input())
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print("No of positive numbers:", pos)
print("No of negative numbers:", neg)
print("No of zeros:", zero)
