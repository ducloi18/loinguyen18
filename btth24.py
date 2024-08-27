# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:13:55 2024

@author: NGUYEN DUC LOI
"""

gio = int(input("Nhập giờ = "))
phut = int(input("Nhập phút = "))
giay = int(input("Nhập giây = "))
if gio > 24 or (phut and giay) > 60:
    print("Thời gian nhập vào không hợp lệ!")
else:
    print(f"Thời gian hợp lệ {gio}/{phut}/{giay}")
