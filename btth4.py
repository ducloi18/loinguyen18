# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:14:22 2024

@author: NGUYEN DUC LOI
"""

N = int(input("Nhập số nguyên dương có hai chữ số = "))
chu_so_hang_chuc = N // 10
chu_so_hang_don_vi = N % 10
tong_hai_chu_so_cua_N = chu_so_hang_chuc + chu_so_hang_don_vi
if 10 <= N <= 99:
    print("Tổng các chữ số của N = ", tong_hai_chu_so_cua_N)
else:
    print("Sai rồi, nhập lại số")
