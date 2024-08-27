# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:23:08 2024

@author: NGUYEN DUC LOI
"""

thoi_gian = input("Nhập thời gian (hh:mm:ss): ")
gio, phut, giay = map(int, thoi_gian.split(":"))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là:", tong_giay)
