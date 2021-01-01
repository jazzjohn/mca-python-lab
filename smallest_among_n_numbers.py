limit = int(input("Enter the limit:"))
print("Enter values:")
smallest = int(input())
for i in range(1, limit):
    num = int(input())
    if num < smallest:
        smallest = num
print("smallest number is:", smallest)
