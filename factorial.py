fact=1
i=1
j=1
while i <= 10:
    while j<=i:
        fact=fact*j
        j=j+1
    print("factorial of "+str(i)+" is "+str(fact))
    i=i+1
    j=1
    fact=1
