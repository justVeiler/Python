# Nhập 1 string, find xem nó có đủ 3 yếu tố : Chữ cái đầu viết hoa & có số & có ký tự đặc biệt hay không'''
# import re
#
# password = str(input("Hay nhap mat khau ma ban thich: "))
#
# check_uppercase_letter = re.findall("^[A-Z]", password)
#
# check_number = re.findall("\d", password)
#
# check_special_letter = re.findall("[^A-Za-z0-9]", password)
#
# if check_special_letter and check_number and check_uppercase_letter:
#     print("Mat khau cua ban da co du bao mat")
# else:
#     print("Nhap lai di ban ei!")

'''
Nhập 1 string, kiểm tra xem có phải số thẻ ATM hay không

import re

string = str(input("Hay nhap so the atm cua ban: "))

check_number = re.findall("[^0-9]", string)

if len(string) != 16 or check_number :
    print("Invalid format ")
else:
    print("Valid format")
'''


'''
Nhập string, kiểm tra xem có phải SDT format : +84xxxxxxxxx hay ko
import re

string = str(input("Hay nhap so dien thoai ma ban muon check: "))

check_areaCode = re.match("^[+]84", string)

if check_areaCode or len(string)!= 12:
    print("Valid Format")
else:
    print("Invalid Format")
'''


