# Get a string from an input string where all occurance  of first charecter replaced with '$' sxcept first charecter

user_str = input("Enter a string:")
lst = list(user_str)
for i in range(len(user_str)):
    j = i + 1
    while j < len(user_str):
        if lst[i].isspace():
            j += 1
            continue
        if lst[i] == lst[j]:
            lst[j] = "$"
        j += 1

print("formatted string is: ", "".join(lst))
