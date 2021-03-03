# write a python programme to read each rows from a given csv file and print a list of strings

import csv
lst=[]
str=()
with open("city.csv","w") as file:
    write=csv.writer(file)
    write.writerow(["place","district","developement"])
    write.writerow(["vatakara","kozhikkode","progress"])
    write.writerow(["mannarkkad", "palakkade", "developing"])
    write.writerow(["Nedumangad","thiruvananthapuram","developed"])
with open("city.csv","r") as file:
    read=csv.reader(file)
    for row in read:
        print(row)
        lst.append(",".join(row))

print(lst)
print(lst[0])

