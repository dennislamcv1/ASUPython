# -*- coding: utf-8 -*-
"""Read_File.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MOtv4aC3egOHblgBEUV1h2d6anZYHHi3
"""

while True:
  try:
    name = input("Please enter file name: ")
    f = open("/content/sample_data/"+name, "r")
    text = f.read() #Reads in entire file as a String
    print(text)
    break
  except IOError:
    print("Please re-enter the file name.")