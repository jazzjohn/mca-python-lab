l = list()
f = open("demo.txt", "w")
f.write("hellowld\n")
f.write("samuel\n")
f.write("vatakara\n")
f.write("kozhikode\n")
f.close()
f = open("demo.txt", "r")
for i in f:
    print(i)
    l.append(i[:-1])
f.close
print(l)
