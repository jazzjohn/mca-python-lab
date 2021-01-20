# list initialisation
list1=["sam","jazz","john"]
list2=list(("jazz","trivandrum","CEV"))

print(list1)
print(list2)

#Adding elements to the list
list2.insert(2,"web developer")
list1[1:3]=[21,"single","vatakara"]

print(list1)
print(list2)

list1.append(1999)
list2.insert(5,2020)

print(list1)
print(list2)

#appending to lists
list1.extend(list2)
print(list1)
print(list2)

#removing elements from list
list1.remove(2020)
print(list1)

list1.pop()
list2.pop(1)
print(list1)
print(list2)

#del keyword
del list2[1]
del list1
print(list2)

#emptying a list
list2.clear()
print(list2)

#loooping a list using for loop
mylist=["sam","jazz",21,"john"]
for x in mylist:
    print(type(x),"->",x)
print("\n")

for x in range(len(mylist)):
    print(mylist[x])
print("\n")

#looping a list using while
i=0
while i<len(mylist):
    print(mylist[i])
    i+=1
print("\n")

#sorting a list
mylist.remove(21)
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

numlist=[10,20,5,25]
numlist.sort()
print(numlist)
numlist.sort(reverse=True)
print(numlist)

#customisable sort function
numlist.extend([55,68,43])
def numfunc(n):
    return abs(n-50)
numlist.sort(key=numfunc)
print(numlist)


#copy list
list1=[1,2,3]
# list2=list1.copy()
# list2=list1
list2=list(list1)
list1.append(4)
print(list1)
print(list2)

