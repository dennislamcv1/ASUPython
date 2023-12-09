# -*- coding: utf-8 -*-
"""PandasDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17NT6ESF6mqfGFnrP5gCTgUSbNWrVxLhf
"""

#Cheet Sheet:
#https://drive.google.com/file/d/1UHK8wtWbADvHKXFC937IS6MTnlSZC_zB/view
#More Examples:
#https://www.geeksforgeeks.org/pandas-tutorial/

import pandas as pd

my_series = pd.Series([4.6, 3.1, -4.0, 3.0])
print(my_series)
print(my_series.values)
print()

city_population = {'New York City': ('NY', 8177025, 8190209,-0.0016,27222,300.381),
                  'Los Angeles': ('CA',3985516,3795512,0.0501,8499,468.956),
                  'Chicago': ('IL',2671635,2697477,-0.0096,11750,227.369),
                  'Houston': ('TX',2325353,2100280,0.1072,3632,640.194),
                  'Phoenix' :('AZ',1759943,1449038,0.2146,3400,517.673)}
dataframe = pd.DataFrame(city_population)
print(dataframe)
print()
city_population = {'name': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
                  'usps': ['NY', 'CA', 'IL', 'TX', 'AZ'],
                  'pop2022': [8177025, 3985516, 2671635, 2325353, 1759943],
                  'pop2010': [8190209, 3795512, 2697477, 2100280, 1449038]}

dataframe = pd.DataFrame(city_population, columns=['name', 'usps', 'pop2022', 'pop2010'])
print(dataframe)
print()

print(dataframe.head(3))
print()
print(dataframe.tail(2))
print()
print(dataframe['name'])
print()
print(dataframe.pop2022 > 8170000)
print()

#/content/sample_data/csvData1.csv

dataframe = pd.read_csv("/content/sample_data/csvData1.csv")
print(dataframe.head(20))
print()

