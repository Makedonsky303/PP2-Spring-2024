# bool(False) 
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})
# all return False

# Operators in Python

# Addition	x + y	
# Subtraction	x - y	
# Multiplication	x * y	
# Division	x / y	
# Modulus	x % y	
# Exponentiation	x ** y	
# Floor division	x // y

# x is y	(Returns True if both variables are the same object)
# x is not y    (Returns True if both variables are not the same object)

# x in y    (Returns True if a sequence with the specified value is present in the object)	
# x not in y    (Returns True if a sequence with the specified value is not present in the object)

# LISTS
# List items are ordered, changeable, and allow duplicate values.

# len(list) − length of the list

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # returns ['cherry', 'orange', 'kiwi']

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # returns ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # returns ['apple', 'banana', 'watermelon', 'cherry']

# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # returns ['apple', 'banana', 'cherry', 'orange']

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # returns ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # returns ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# Remove Specified Item
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) # returns ['apple', 'cherry', 'banana', 'kiwi']

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # returns ['apple', 'cherry']
# If you do not specify the index, the pop() method removes the last item.

# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # returns []

# Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# Shortest form:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Sorting by property
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) # ['apple', 'banana', 'mango'] all consist letter 'a'

# Short form

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]


# Example
# Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

# Example
# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]


# Sort the list alphabetically or numerically:

thislist.sort()

# To sort descending, use the keyword argument reverse = True:

thislist.sort(reverse = True)


# Customize Sort Function
# Sort the list based on how close the number is to 50:

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)


# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # returns ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()


# Some ways to join two list

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

# or

for x in list2:
    list1.append(x)
print(list1)

# or

list1.extend(list2)
print(list1)


# tuple 
thistuple = ("apple", "banana", "cherry")
# List items are ordered, changeable, and allow duplicate values.

