"""1. Write a Python program which accepts the user's first and last name and prints them in
reverse order with a space between them."""

firstname= "Rohini"
lastname= "Yadav"
print (lastname[::-1] +" " + firstname[::-1])

"""2. Write a Python program which accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23"""

value="3,5,7,23"
list= value.split(",")
tuple= tuple(list)
print('List : ' ,list)
print('Tuple : ' ,tuple)


"""3.Write a Python program to display the first and last colours from the following list.
color_list = ["Red","Green","White" ,"Black"]"""

color_list = ["Red","Green","White" ,"Black"]
print("first element is",color_list[0],"last element is",color_list[-1])

"""4. Write a Python program to print the documents (syntax, description etc.) of Python built-in
function(s).
Sample function : abs()
Expected Result : mat
abs(number) -> number
Return the absolute value of the argument."""

print(abs.__doc__)

"""5. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module."""

import calendar
y= int(input("Input the year : "))
m= int(input("Input the month : "))
print(calendar.month(y, m))

"""6. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"""

import datetime as dt
k = dt.datetime (2022,12,7) 
r = dt.datetime (2022,12,29)
rk = r-k
print (rk)

"""7. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""


def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))

"""10. Write a Python program to print out a set containing all the colors from color_list_1 which are
not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :

{'Black', 'White'}"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))
