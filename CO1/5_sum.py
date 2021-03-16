num = input("Enter a number:")
str = ""
flag = 0
for i in range(3):
    if flag:
        str += "+"
    else:
        flag = 1
    for j in range(i + 1):
        str += num

print(str)
