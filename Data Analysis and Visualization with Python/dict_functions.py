# -*- coding: utf-8 -*-
"""Dict_Functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sxxXnCtRJQqMCFrwOi2ekgMTIk70rN59
"""

dictionary1 = {'firstName': 'Sam', 'lastName': 'Simpson', 'Age': 19}
print(len(dictionary1)) #Prints the number of sets in the dictionary
print()
print(str(dictionary1)) #printable String of the dictionary
print()
print('Sam', type(dictionary1))
print()
print(dictionary1.get('Age')) #gets the value tied to age
print()
print(dictionary1.items()) # Returns the values in tuple pairs
print()
print(dictionary1.keys()) #Displays the key values
print()