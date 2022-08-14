"""
     Array

1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes."""

from array import *
array_num = array('b', [1,3,5,7,9])

for b in array_num:
    print(b)

print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])

"""2. Write a Python program to reverse the order of the items in the array."""


arr = [1, 7, 3, 9, 5];     
print("Original array: ");    
for i in range(0, len(arr)):    
    print(arr[i]),     
print("Array in reverse order: ");    

for i in range(len(arr)-1, -1, -1):     
    print(arr[i]),     
    
    
"""
        Dictionary

2.Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""

r= {0:10, 1:20}
print(r)
r.update({2:30})
print(r)

"""3. Write a Python script to concatenate following dictionaries to create a new
one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60}  
dic4 = {}  
for d in (dic1, dic2, dic3): dic4.update(d)  
print(dic4)  

"""9. Write a Python program to print a dictionary in table format."""

my_dic={'C1':[3,2,5],'C2':[7,8,9],'C3':[5,1,4]}
for row in zip(*([key] + (value) for key, value in sorted(my_dic.items()))):
    print(*row)
    
"""11. Write a Python program to convert a list into a nested dictionary of keys."""
        
lst= [1, 2, 3, 4]
dct= current = {}
for name in lst:
    current[name] = {}
    current = current[name]
print(dct)

"""12. Write a Python program to check multiple keys exists in a dictionary."""

student= {
  'name':'Rohini',
  'class':'CSBS',
  'roll_id':'61'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Rohini'})
print(student.keys() >= {'roll_id', 'name'})

"""13. Write a Python program to count number of items in a dictionary value
that is a list."""

dict =  {'Rohini': ['subj1', 'subj2'], 'Khushi': ['subj1']}
rj = sum(map(len, dict.values()))
print(rj)

"""
    Sets
    
1. Write a Python program to create a set."""

s=set(['Delhi', 'Mumbai', 'Bangalore', 'Pune', 'Jaipur', 'Ladakh'])
print(s)
print(type(s))

"""3.Write a Python program to add member(s) in a set."""

color=set()
color.add("Red",)
print(color)
color.update(["Blue", "Yellow" ,"Green"])
print(color)    

"""5. Write a Python program to create an intersection of sets."""


setx= set(["green", "blue"])
sety= set(["blue", "yellow"])
print("\nOriginal set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx & sety
print(setz)

"""12. Write a Python program to find maximum and the minimum value in a set."""

def MAX(sets):
    return (max(sets)) 
sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(MAX(sets))

def MIN(sets):
    return (min(sets))
sets = set([4, 12, 10, 9, 4, 13])
print(MIN(sets))

"""List
1. Write a Python program to sum all the items in a list."""

total = 0
list1 = [11, 5, 17, 18, 23]
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("\nSum of all elements in given list: ", total)

"""7. Write a Python program to clone or copy a list."""

lst=[10, 22, 44, 23, 4]
new_lst=list(lst)
print(list)
print(new_lst)
