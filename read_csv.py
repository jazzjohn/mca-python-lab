import csv
lst=[]
str=()
with open("city.csv","w") as file:
    write=csv.writer(file)
    write.writerow(["achu","sachu","sanu"])
with open("city.csv","r") as file:
    read=csv.reader(file)
    for row in read:
        print(row)
        lst.append(",".join(row))

print(type(lst[0]))

