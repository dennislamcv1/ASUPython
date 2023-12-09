# -*- coding: utf-8 -*-
"""Pandas_MergeJoin.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FutaLA-eQCJgHW_1lCScG4jn1AmI_Ns1
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
             }, index=[10, 20, 30, 40, 50, 60] )

conference3 = pd.DataFrame({'Year':[1,2,3,4,5,6], 
             "Profit":[1320, 921,967,1410,1405,1310], 
             }, index=[10, 30, 40, 60, 70, 90] )

print(conference2)
print()
print(pd.merge(conference1, conference2))

print()
print(pd.merge(conference1, conference2, on="Overall Rating"))

print()
joined= conference1.join(conference3)
print(joined)