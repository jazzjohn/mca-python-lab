t=("orange","apple","banana","appple","cherry")
print(t[-1])
print(t[2:5])
print(len(t))
print(type(t))

#tuple constructor
t2=tuple(("samuel",21,1999,"single"))
print(t2)

#change tuple value
t=("a",'B','c')
print(t)
l=list(t)
l[1]='b'
l.append('d')
t=tuple(l)
print(t)

#unpacking
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green,yellow,red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green,tropic,red)
