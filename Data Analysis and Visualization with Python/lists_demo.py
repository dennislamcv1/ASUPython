# -*- coding: utf-8 -*-
"""lists_Demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zwOe82cJITgFRbk9Zq_lTw62gx1YZ-0P
"""

#Exercise 1
#Create a list with different data types
list1 = [23, "Bob", 'Tina', 23.4]

print(list1)

#Exercise 2
#Write a program to display all the elements in a list
list1 = [21, 45, 32, 20, 31, 30, 45, 67, 110]
for i in range(len(list1)):
    print(list1[i])

#Exercise 3
#Write a program to count the number of items in the list
list1 = [21, 45, 32, 20, 31, 30, 45, 67, 110]
count = 0;
for i in range(len(list1)):
  count = count + 1;

print("I have a total of", count, "Elements")

print(len(list1))

#Exercise 4
#Write a program to square each element in a list
list1 = [21, 45, 32, 20, 31, 30, 45, 67, 110]

for i in range(len(list1)):
  list1[i] = list1[i] * list1[i]

print(list1)

#Exercise 5
#Write a program to append each element to a list (request the value from user)
list1 = [21, 45, 32, 20, 31, 30, 45, 67, 110]

x = input("Please enter item to insert: ")
list1.append(x)

print(list1)

#Exercise 6
#Write a program to display the values that are divisible by 5
list1 = [21, 45, 32, 20, 31, 30, 45, 67, 110]

for i in range(len(list1)):
  if(list1[i] % 5 == 0):
    print(list1[i])
  else:
    pass