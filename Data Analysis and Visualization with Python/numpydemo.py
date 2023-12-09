# -*- coding: utf-8 -*-
"""NumpyDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wATIWEQkCNZ0ReT3QjUUV5T7dwV1omoI
"""

import numpy as np

a = np.array([[1,2,3], [3,4,5]]) # Array of ints
print(a)
print()
b = np.array([[1.1, 2.2, 3.3], [3.3, 4.4, 5.5]]) #Array of Floats
print(b)
print()
c = np.array([[1,2,3], [3,4,5]], dtype = complex)
print(c)
print()
d = np.zeros((4,6))
print(d)
print()
e = np.arange(12)
print(e)
print()
f = e.reshape(3,4)
print(f)
print()
print("a[1] = ", a[0][0])
print("a[0][1]=", a[0][1])
print("a[-1]", a[1][0] )
print(a+b)
print()
b = np.array([[1.1, 2.2, 3.3], [3.3, 4.4, 5.5], [6.6,7.7,8.8]]) 
print(np.dot(a,b))
print()
a = np.array([[1,2,3,4,5,6], [3,4,5,6,7,8],[5,6,7,8,9,10]]) # Array of ints
print(a[:2, :4])
print()
print(a[:1,])
print()
print(a[ :, 2:5])
