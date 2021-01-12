fact = 1
for i in range(1, 11):
    for j in range(1, i + 1):
        fact = fact * j
    print("factorial of ", i, " is ", fact)
    fact = 1
