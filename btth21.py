# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:08:15 2024

@author: NGUYEN DUC LOI
"""

num = int(input("Nhập một số nguyên: "))
if num == 0:
    print("Không")
elif num == 1:
    print("Một")
elif num == 2:
    print("Hai")
elif num == 3:
    print("Ba")
elif num == 4:
    print("Bốn")
elif num == 5:
    print("Năm")
elif num == 6:
    print("Sáu")
elif num == 7:
    print("Bảy")
elif num == 8:
    print("Tám")
elif num == 9:
    print("Chín")
else:
    print("Không đọc được")


dinh_dang = {
    0: "Không",
    1: "Một",
    2: "Hai",
    3: "Ba",
    4: "Bốn",
    5: "Năm",
    6: "Sáu",
    7: "Bảy",
    8: "Tám",
    9: "Chín"
}
nhap = int(input("Nhập một số nguyên: "))
if nhap in dinh_dang:
    print(dinh_dang[nhap])
else:
    print("Không đọc được")
