# -*- coding: utf-8 -*-
"""Set_Methods2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10SD5LvmTE8DjT0OpU4-M8ayQAl4wbO4p
"""

set1 = {11, 22, 33, 44, 55} #Creates a Set
set2 = {11, 33, 55, 77, 99} #Creates a Set

print(set1.union(set2)) #Combines all elements in both sets
print()
print(set1.intersection(set2)) #Prints only the elements in both sets
print()
print(set1.difference(set2)) #Prints only the elements that are not in both sets
print()
print(set1.isdisjoint(set2)) #Return True if two sets have a null intersection
print()
print(set1.issubset(set2)) #Return True if another set contains this set
print()
print(set1.issuperset(set2)) #Return True if this set contains another set
print()
set1.discard(55)
print(set1)