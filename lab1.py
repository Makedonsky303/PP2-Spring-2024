print("text", 256 , 3.1415 , False) # function print() outputs texts to the console

if 2+2==5:
  print("some text") # we have to indent this part of code

# It's a simple comment    
"""It's 
multiline 
comment"""
# print("The code doesn't work here")

# The main types of variables
x = 1 # int
y = 1.0 # float
z = "1" # str
w = 1 + 1j # complex
b = True # bool
my_list = [1 , 2 , 3] # list
my_dict = {"name":"James","surname":"Bond"} # dict
my_tuple = (1,2,3) # tuple

print(type(x))
print(type(y))
print(type(z))
print(type(b))
print(type(w))
print(type(my_list))
print(type(my_dict))
print(type(my_tuple))


# The rules for creating variables

# 1) Use only English alphabet, digits or underscores. No spaces
# 2) The first character is letter or underscore, not a number
# 3) The variable can't be a Python keyword
# 4) JAMES and james are different variables
# 5) Of course, don't create the same variables

# Styles of Multi Words Variable Names

# 1) Camel Case: myVariableName
# 2) Pascal Case: MyVariableName
# 3) Snake Case: my_variable_name


# Many Values to Multiple Variables
x, y, z = "x", "y", "z"

# One Value to Multiple Variables
x = y = z = "the same value"

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# Global and local variables
x = "awesome"

def myfunc():
  x = "easy"
  print("Python is " + x)

myfunc()
print("Python is " + x)


# Random number
import random
print(random.randrange(1, 10)) # random number between 1 and 9:


# Casting
# int(value) ; value can be float or str type
# float(value) ; value can be int or str type
# str(value) ; value can be int or float type

# Multiline strings
string = """This string
is multiline"""

# Length of strings
length = len(string)

# Operator "in" and "not in"
txt = "The best things in life are free!"
print("free" in txt)
print("free" not in txt)


# Slicing strings
sentence = "KBTU is great"
print(sentence[:8] + sentence[-5:])

# Modify Strings

# string.upper() - "abc" -> "ABC"

# string.lower() - "ABC" -> "abc"

# string.strip() - " Abc " -> "Abc"

# string.replace(old, new) - "old old" -> "new new"

# Spliting string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Joining string
my_list2 = ['Hello', ' World!']
print(",".join(my_list2)) # returns Hello, World!

# Format - Strings
age = 19
name = "Iskander"
txt = "My name is {}, and I am {}"
print(txt.format(name,age))

# Escape Characters

mystr = "You can put \"some quote here\" "
