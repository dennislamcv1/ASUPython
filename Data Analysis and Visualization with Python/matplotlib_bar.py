# -*- coding: utf-8 -*-
"""Matplotlib_Bar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NYwl1o9MC8DJyTUfsOqAIN_AG2Lp8CIJ
"""

import matplotlib.pyplot as plt
import numpy as np

company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]

xpos = np.arange(len(company))

profit=[40,2,34,12]
plt.bar(xpos-0.2,revenue, width=0.4, label="Revenue")
plt.bar(xpos+0.2,profit, width=0.4,label="Profit")

plt.xticks(xpos,company)
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()