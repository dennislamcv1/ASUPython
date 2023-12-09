# -*- coding: utf-8 -*-
"""Matplotlib_Scatter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tnrQ3qUMSDS0dfwT_MRnaPI7Fm9qUreF
"""

import matplotlib.pyplot as plt

x= [22,33,44,32,12,12,543,23,432,237,445,533,343,353,653,345,453,475,443,476]
y= [23,414,413,656,344,23,234,213,543,343,345,543,234,424,322,345,34,543,234,234]

plt.scatter(x,y, label='Scatter Plot', marker="x")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot Data')
plt.legend()
plt.show()