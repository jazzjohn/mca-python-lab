list=[]
List2=[]

limit=int(input("Enter the limit:"))
for i in range(limit):
    list.append(int(input("Enter a number:")))
print("The entered list is:",list)

List2.extend(list)

for i in list:
    if i % 2 == 0:
        List2.remove(i)

print(" list after removing even numers is:",List2)
