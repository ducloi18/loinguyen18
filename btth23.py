# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:44:01 2024

@author: NGUYEN DUC LOI
"""
import math
a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
denta = b*b - (4*a*c)
if a == 0:
    print(" pt có 1 nghiệm duy nhất x=", -b/c)
elif a != 0 and denta < 0:
    print(" pt vô nghiệm")
elif a != 0 and denta == 0:
    print("pt có nghiệm kép x1=x2 = ", -b/(2*a))
elif a != 0 and b*b-(4*a*c) > 0:
    print("pt có 2 nghiệm pb x1 = ", (-b + math.sqrt(denta))/(2*a))
    print("pt có 2 nghiệm pb x2 = ", (-b - math.sqrt(denta))/(2*a))
