# -*- coding: utf-8 -*-
"""Pandas_Concat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eglx3w_gWyLe4B8SOgk7bWVGEHPYimDY
"""

import pandas as pd

conference1= pd.DataFrame({'Day':[1,2,3,4,5,6], 
             "Attendies":[1320, 921,967,1410,1405,1310], 
             "Overall Rating":[5,4.2, 4.1,3.8,4.6,4.4]
             }, index=[10, 20, 30, 40, 50, 60]) 
print(conference1)
print()
conference2= pd.DataFrame({'Day':[1,2,3,4,5,6], 
             "Attendies":[1320, 921,967,1410,1405,1310], 
             "Overall Rating":[4.2,4.2, 4.0,3.8,4.6,4.4]
             }, index=[70, 80, 90, 100, 110, 120] )
print(conference2)
print()
print(pd.concat([conference1, conference2]))