# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:16:06 2024

@author: NGUYEN DUC LOI
"""
a = float(input(" nhập số a: "))
b = float(input(" nhập số b: "))
if a == 0 and b == 0:
    print(" pt có vô số nghiệm")
elif a == 0 and b != 0:
    print(" pt vô nghiệm")
else:
    print(" pt có 1 nghiệm x=", -b/a)
