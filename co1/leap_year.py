currentYear=2020
futureYear=int(input("Enter a future year:"))
print("The leap years form 2020 to entered year are:")
for x in range(currentYear,futureYear+1):
    if x % 4 == 0:
        if x % 100 == 0:
            leapyear = "true"
            if x % 400 == 0:
                leapyear = "true"
            else:
                leapyear = "false"
        else:
            leapyear = "true"
    else:
        leapyear = "false"

    if leapyear == "true":
        print(x)

