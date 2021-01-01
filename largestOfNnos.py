large = 0
limit = int(input("Enter the limit:"))
print("Enter values:")
for i in range(1, limit + 1):
    num = int(input())
    if num > large:
        large = num
print("largest number is:", large)
