# -*- coding: utf-8 -*-
"""ReadingFileSplit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WWfedqv_Yxb_6teafGulk_94hLhbw57f
"""

f = open("/content/sample_data/hello.txt", "r")
text = f.read() #Read in entire file as a String
for x in text.split():
  print("x = " + x)