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

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# LISTS
# List items are ordered, changeable, and allow duplicate values.

# len(list) − length of the list

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

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
# List items are ordered, unchangeable, and allow duplicate values.

# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

# Tuple items can be of any data type

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# as well as with lists we can use len() function,"in" and "not in" operators; here are the same element accesing, 
# negative indexing,range of indexes

# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x) 
y[1] = "kiwi" # we can do another manipulations in order to change list
x = tuple(y)

print(x)


# You are allowed to add tuples to tuples.
# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name 
# and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) # apple
print(yellow) # banana
print(red) # ['cherry', 'strawberry', 'raspberry']


# If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number 
# of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) # apple
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red) # cherry

# Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# you can also use "Loop Through the Index Numbers" and while loop
  
# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  

# Multiply the fruits tuple by 2

mytuple = fruits * 2

print(mytuple)

# Tuple Methods
# count() Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


# Defining a Set
myset = {"apple", "banana", "cherry"}
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) # returns {True, 2, 'banana', 'cherry', 'apple'}
# False and 0 is considered the same value

# use len() to get length of a set
# A set can contain different data types:


# Access Items
# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Check if "banana" is present in the set:

print("banana" in thisset)  

# Add an item to a set, using the add() method:

thisset.add("orange")

# To add items from another set into the current set, use the update() method.

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
# The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).


# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")
thisset.discard("banana")
# Note: If the item to remove does not exist, 
# remove() will raise an error, dicard() will not.

# You can also use the pop() method to remove an item, 
#but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

# The clear() method empties the set

# The del keyword will delete the set completely

for x in thisset:
  print(x)



# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# The intersection_update() method will keep only the items 
# that are present in both sets.
x.intersection_update(y)
print(x)

# The intersection() method will return a new set, 
# that only contains the items that are present in both sets.
z = x.intersection(y)
print(z)


# The symmetric_difference_update() method will keep only the elements 
# that are NOT present in both sets. 

# The symmetric_difference() method will return a new set, 
# that contains only the elements that are NOT present in both sets.



# Defining Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Print the "brand" value of the dictionary:
print(thisdict["brand"])


# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# To determine how many items a dictionary has, use the len() function

# Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Get the value of the "model" key:

x = thisdict.get("model")

# Get a list of the keys:

x = thisdict.keys()


# Add a new item to the original dictionary, 
# and see that the keys list gets updated as well:

x = thisdict.keys()

print(x) #before the change

thisdict["color"] = "white"

print(x) #after the change

# Get a list of the values:

x = thisdict.values()
# Just like keys() method , values() also gets updated


# The items() method will return each item in a dictionary,
# as tuples in a list.
x = thisdict.items()

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# You can change the value of a specific item by referring to its key name:

# ExampleGet your own Python Server
# Change the "year" to 2018:

thisdict["year"] = 2018 
thisdict.update({"year": 2020})


# The pop() method removes the item with the specified key name:
thisdict.pop("model")

# The popitem() method removes the last inserted item
thisdict.popitem()

# The del keyword removes the item with the specified key name or even whole dictionary:
del thisdict["model"]
del thisdict

# The clear() method empties the dictionary

# Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])  


# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

# Make a copy of a dictionary with the copy() method or dict function:
mydict = thisdict.copy()
mydict = dict(thisdict) 


# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Print the name of child 2:

print(myfamily["child2"]["name"])

