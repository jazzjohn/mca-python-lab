# construct the pattern using nested loop

for i in range(1, 10):
    j = 1
    if i > 5:
        limit = i - ((i % 5) + (i % 5))
    else:
        limit = i
    while (j <= limit):
        print(end="*")
        j += 1
    print(end="\n")


# for i in range(9):
#     if (i <= 4):
#         j = 0
#         while j <= i:
#             print(end='*')
#             j += 1
#         print(end='\n')
#     else:
#         j = 8
#         while j >= i:
#             print(end='*')
#             j -= 1
#         print(end='\n')
