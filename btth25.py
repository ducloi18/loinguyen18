# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:28:35 2024

@author: NGUYEN DUC LOI
"""

nhap = input("Nhập 1 chữ cái: ")
if len(nhap) == 1:
    if nhap.lower:
        print(nhap.upper())
    elif nhap.upper():
        print(nhap.lower())
    else:
        print("Không nhận diện được")
else:
    print("Không hợp lệ")
