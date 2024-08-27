# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:28:30 2024

@author: NGUYEN DUC LOI
"""

a = int(input("Nhập số nguyên a = "))
b = int(input("Nhập số nguyên b = "))
tong = a + b
hieu = a - b
tich = a * b
thuong = round(a / b, 3)
print("tổng hai số = ", tong)
print("hiệu hai số = ", hieu)
print("tich hai số = ", tich)
print("thương hai số = ", thuong)
print("thương hai số = ", round(a / b, 2))
kq_chia_nguyen = a // b
kq_chia_du = a % b
print("Kết quả chia được phần nguyên = ", kq_chia_nguyen)
print("Kết quả chia được phần dư = ", kq_chia_du)
