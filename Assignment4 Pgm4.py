# -*- coding: utf-8 -*-
"""Copy of Untitled55.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HqI8q956YcGRl0xbiFl1nGPqGqLBwm0d
"""

def compute_hcf(x, y):
 
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
 
num1 = 25
num2 = 50
 
print("The H.C.F is", compute_hcf(num1, num2))