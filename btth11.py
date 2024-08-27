# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:59:58 2024

@author: NGUYEN DUC LOI
"""

chu_thuong = input("Nhập 1 kí tự chữ thường: ")
if len(chu_thuong) == 1 and chu_thuong.islower():
    chu_hoa = chu_thuong.upper()
    print("Chữ in hoa của kí tự nhập vào là: ", chu_hoa)
else:
    print("Vui lòng nhập đúng kí tự thường")
