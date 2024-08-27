# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:21:10 2024

@author: NGUYEN DUC LOI
"""

ngay_thang_nam = input("Nhập ngày tháng năm(dd mm yyyy): ")
dd, mm, yyyy = ngay_thang_nam.split(" ")
print(f"{dd}/{mm}/{yyyy}")
print(f"{dd}/{mm}/{(yyyy)[2:]}")
print(f"{yyyy}/{mm}/{dd}")

input_a = input("Nhập theo định dạng Ngày/Tháng/Năm: ")
input_b = input("Nhập theo định dạng Ngày/Tháng/2 số cuối của Năm: ")
input_c = input("Nhập theo định dạng Năm/Tháng/Ngày: ")
day_a, month_a, year_a = map(int, input_a.split('/'))
day_b, month_b, year_b = map(int, input_b.split('/'))
year_b += 1900 if year_b > 50 else 2000
year_c, month_c, day_c = map(int, input_c.split('/'))
print("Kết quả từ định dạng a:", day_a, month_a, year_a)
print("Kết quả từ định dạng b:", day_b, month_b, year_b)
print("Kết quả từ định dạng c:", day_c, month_c, year_c)
