# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:05:47 2024

@author: NGUYEN DUC LOI
"""

a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
max_value = a
if max_value < b:
    max_value = b
if a < c:
    max_value = c
print(max_value)
