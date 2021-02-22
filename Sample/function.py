# sum of elements in list
l = [12, 24, 48, 36]

def sumlist(l):
    sum = 0
    for i in l:
        sum += i
    return sum

print(sumlist(l))

# adding two elements
a=10
b=11
def add(x,y):
    return x+y

print(add(a,b))

# return a string
def word():
    return "jazz"
print(word())

# keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#arbitrary arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# keyword arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# defualt value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# lambda function
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))