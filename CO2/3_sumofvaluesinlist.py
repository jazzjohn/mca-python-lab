# find the sum of all the items in a list

list = []
sum = 0
limit = int(input("Enter the limit:"))
for i in range(limit):
    list.append(int(input("Enter number " + str(i + 1) + ":")))
print(list)

for i in list:
    sum = sum + i;
print("sum of elements in the list is:", sum)
