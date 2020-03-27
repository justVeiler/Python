# '''Nhập 1 string, find xem nó có đủ 3 yếu tố : Chữ cái đầu viết hoa & có số & có ký tự đặc biệt hay không'''
import re

password = str(input("Hay nhap mat khau ma ban thich: "))

check_uppercase_letter = re.findall("^[A-Z]", password)

check_number = re.findall("\d", password)

check_special_letter = re.findall("[^A-Za-z0-9]", password)

if check_special_letter and check_number and check_uppercase_letter:
    print("Mat khau cua ban da co du bao mat")
else:
    print("Nhap lai di ban ei!")
