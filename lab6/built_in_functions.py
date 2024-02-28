#1
from functools import reduce

numbers_list = [2, 3, 4, 5]

print("Result:", reduce(lambda x,y:x*y, numbers_list))

#2
# my_str = "ABcde"

# lower_num = 0 
# upper_num = 0

# for i in my_str:
#     if i.islower():
#         lower_num+=1
#     elif i.isupper():
#         upper_num+=1
# print("Amount of lower case letters is {}, amount of upper is {}".format(lower_num,upper_num))     

#3
# def isPalindrome(this_string):
#     return this_string==this_string[::-1]
# print(isPalindrome("madam"))

#4
# from time import sleep 
# num = float(input("Input: "))
# miliseconds = int(input("Miliseconds: "))

# sleep(miliseconds/1000)
# print("Square root of {0} after {1} miliseconds is {2}".format(num,miliseconds,num**0.5))

#5
# my_tuple = (True, 1 , "a")

# print(all(my_tuple))