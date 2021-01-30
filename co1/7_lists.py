# def takeInput(list):
#     limit=int(input("Enter the limit:"))
#     for x in range(limit):
#         num=int(input("Enter number "+str(x+1)+":"));
#         list.append(num)


# def whetherSameLenght(l1,l2):
#     if len(l1)==len(l2) :
#         print("The two entered strings are equal");
#
# def sum(l,sum):
#     for x in l:
#         sum=sum+l[x]
#     return sum;
#
# def whetheAnyValueOccurInBoth(l1,l2):
#     f=0
#     for x in l1:
#         for y in l2:
#             if(l2[y]==l1[x]):
#                 f=1
#                 break
#         if(f==1):
#             break
#     if(f==0):
#         print("The two lists have no same values")
#     else:
#         print("The two lists have same value")


list1=list()
list2=list()
sum1=0
sum2=0


#Inputing values into the list
limit = int(input("Enter the limit:"))
for x in range(limit):
    num = int(input("Enter number " + str(x + 1) + ":"));
    list1.append(num)

limit = int(input("Enter the limit:"))
for x in range(limit):
    num = int(input("Enter number " + str(x + 1) + ":"));
    list2.append(num)

print(list1)
print(list2)

#checking whether lists are of same lenght
if(len(list1)==len(list2)):
    print("Two lists are of same length\n")
else:
    print("Two lists are of different length\n")

for i in list1:
    sum1=sum1+i

for i in list2:
    sum2=sum2+i

print(sum1)
print(sum2)
#check wether sum of two lists are same
if(sum1==sum2):
    print("sum of elements in 2 lists are same\n")
else:
    print("sum of elements in 2 lists are not same\n")

#chech whether same value occur in the lists
f = 0
for x in list1:
    for y in list2:
        if (y == x):
            f = 1
            break
    if (f == 1):
        break
if (f == 0):
    print("The two lists have no same values\n")
else:
    print("The two lists have same values\n")




