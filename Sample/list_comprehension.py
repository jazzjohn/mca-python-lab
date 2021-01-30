a=[1,2,3,4,5]
# b=[]
# for i in a:
#     b.append(i**2)
# print(b)

b=[i**2 for i in a]
print(b)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

list=[i+1 for i in range(10) if i<5]
print(list)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

name=["hello" for i in fruits]
print(name)