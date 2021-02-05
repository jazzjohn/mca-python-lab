# loop through string
s='orange'
for i in s:
    print(i)

# multiline string
s1='''my name is jazz john
     I an 21 years old'''
print(s1)

# in keyword
txt = "The best things in life are free!"
print("free" in txt)

# in keyword with if
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# slicing
b="hello, world"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[:-1])
print(b[-5:-2])

# buit-in functions in string
s="   samuel jazz JOHN  "
print(s.upper())
print(s.strip())
print(s.lower())
print(s.replace("jazz","j jazz"))

# split
s.strip()
print(s.split());
s="hello, world"
print(s.split(','));

# string concatenation
a="hello"
b="world"
print(a+" "+b)

# string format
age=21
string="I am {} years old"
print(string.format(age))

item=21
quantity=10
price=100
product="There is {} items which each contain {} quantity with {} rupees"
print(product.format(item,quantity,price))
product="There is {1} items which each contain {0} quantity with {2} rupees"
print(product.format(item,quantity,price))

# printing escape characters
print("My name is \"Samuel Jazz John\"")

