# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:02:44 2024

@author: NGUYEN DUC LOI
"""

can_nang = float(input("Nhập số cân của bạn(kg) = "))
chieu_cao = float(input("Nhập chiều cao của bạn(m) = "))
BMI = can_nang / (chieu_cao * chieu_cao)
print("Chỉ số BMI của bạn = ", round(BMI, 1))
