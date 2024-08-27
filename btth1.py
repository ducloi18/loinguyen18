# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:25:49 2024

@author: NGUYEN DUC LOI
"""

num_a = int(input("Nhập số nguyên a = "))
num_b = int(input("Nhập số nguyên b = "))
num_c = int(input("Nhập số nguyên c = "))
num_d = int(input("Nhập số nguyên d = "))
numbers = (num_a, num_b, num_c, num_d)
average = sum(numbers) / len(numbers)
print("trung bình cộng của 4 số = ", average)
