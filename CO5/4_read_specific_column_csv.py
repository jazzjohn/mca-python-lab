# write a programme to read specific columns of a given csv file and print the content of the column

import csv

header=["place","name","age"]
with open("city.csv","w") as file:
    write=csv.DictWriter(file,fieldnames=header)
    write.writeheader()
    write.writerow({"vatakara","Samuel",21})
    write.writerow({"kainatty", "Aswanth", 21})
    write.writerow({"Tholikkode","Rojin", 23})
    write.writerow({"Palakkaadu", "Aleena", 13})
with open("city.csv","r") as file:
    read=csv.DictWriter(file);
    n=input("Enter the column name you want:")
    for i in read:
        print(read[n])