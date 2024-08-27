# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:12:16 2024

@author: NGUYEN DUC LOI
"""

# In ra menu
print("============ MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("==============================")
khach_chon = input("Mời bạn nhập lựa chọn: ")
print("==============================")
if khach_chon == 1:
    print("Món bạn chọn là Hủ tiếu")
elif khach_chon == 2:
    print("Món bạn chọn là Cháo lòng")
elif khach_chon == 3:
    print("Món bạn chọn là Bánh canh")
elif khach_chon == 4:
    print("Món bạn chọn là Bún riêu")
elif khach_chon == 5:
    print("Món bạn chọn là phở bò")
else:
    print("Món bạn chọn không hợp lệ")
