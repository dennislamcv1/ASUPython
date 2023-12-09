# -*- coding: utf-8 -*-
"""UsingSetsDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16fgwJTj5oOEqSBY_QebdP2RklXNQXflW
"""

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

a.add(5)
print(a)
a.remove(5)
print(a)
a.discard(3)
print(a)
a.add(3)
print(a)
a.pop()
print(a)
a.clear()
print(a)

a = {1, 2, 3, 4}
print(a.union(b, c, d)) #Set union can be performed with the | operator
print(a | b)

print(a.intersection(b, c, d)) #Compute the intersection of two or more sets.
print(a & b & c & d)

print(a.difference(b, c, d))#Compute the difference between two or more sets.
print(a - c)

print(a.symmetric_difference(b))#Compute the symmetric difference between sets.
print(a ^ b ^ c)

print(a.issubset({1,2,3,4,5,6,7,8})) #Determine whether one set is a subset of the other.
print(a <= b)
print(a < b) #Determines whether one set is a proper subset of the other.

print(a.issuperset({2,3}))#Determine whether one set is a superset of the other.
a |= b

print(a)#Modify a set by union.

a = {1, 2, 3, 4}

a &= b
print(a)#Modify a set by intersection.

a = {1, 2, 3, 4}

a -= b
print(a)#Modify a set by difference.

a = {1, 2, 3, 4}
a ^= b
print(a)#Modify a set by symmetric difference.

a = {1, 2, 3, 4}
print(len(a))