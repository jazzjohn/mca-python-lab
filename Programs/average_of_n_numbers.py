total = 0
limit = int(input("Enter the limit:"))
print("Enter the values:")
for i in range(1, limit + 1):
    num = int(input())
    total += num
print("Average of given numbers is:", total / limit)
