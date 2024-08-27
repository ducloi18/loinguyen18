# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:16:10 2024

@author: NGUYEN DUC LOI
"""

from datetime import datetime
nam_sinh = int(input("Nhập năm sinh của bạn là (yyyy): "))
nam_hien_tai = datetime.now().year
tuoi_cua_ban = nam_hien_tai - nam_sinh
print("Số tuổi của bạn là: ", tuoi_cua_ban)
