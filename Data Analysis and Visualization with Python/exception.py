# -*- coding: utf-8 -*-
"""Exception.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mMCkTryETJhPqDdd5SjkwOSYM2flvXjd
"""

while True:
  try:
    x = int(input("Please enter a number: "))
    break
  except ValueError:
    print("Invalid number... Please try again.")
  else:
    print("Unkown Error occured.")