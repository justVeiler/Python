# Bai tap Nhap ten tuoi & so sanh
# maxAge = 0
# maxName = ""
# for i in range(3):
#     inputName = str(input("Hay nhap ten nguoi thu {}: ".format(i + 1)))
#     inputAge = int(input("Hay nhap so tuoi cua nguoi do: "))
#     if inputAge > maxAge:
#         maxAge = inputAge
#         maxName = inputName
#
# print(maxName)
# print(maxAge)

# Bai tap nhap ten tuoi & so sanh dung List

'''
inputName = ""
inputAge = ""

listLength = 3

listAges = [0] * listLength
listNames = [''] * listLength

for i in range(listLength):
    inputName1 = str(input("Hay nhap ten nguoi thu {}: ".format(i + 1)))
    inputAge1 = int(input("Hay nhap tuoi nguoi do: "))
    listAges[i] = inputAge1
    listNames[i] = inputName1

theOldest = max(listAges)
position = listAges.index(max(listAges))
print("Nguoi thu {} la nguoi nhieu tuoi nhat".format(position))
'''

# 0805 : BT List https://v1study.com/c-bai-tap-phan-mang-array-a494.html
# Bai tap phan chuoi :
import re
import sys

my_List = str(input("Hay nhap 1 chuoi ky tu ma ban thich: "))

'''random length of a string'''
# if 0 < len(my_List) < 50:
#     print("chuoi cua ban co {} ky tu".format(len(my_List)))
# else:
#     print("Vuot qua so ky tu cho phep, toi da 50 ky tu")
#
'''find all digits character '''
# check_Number = re.findall("\d", my_List)
# if check_Number:
#     print("Chuoi cua ban co cac ky tu so la {}".format(check_Number))
# else:
#     print("Chuoi cua ban khong co ky tu so nao")
#
'''find all upper case letter'''
# check_Letter = re.findall("[A-Z]", my_List)
# if check_Letter:
#     print("Chuoi cua ban co cac ky tu {}".format(check_Letter))
# else:
#     print("Chuoi cua ban khong co tu in hoa")

''' find a random char in string '''
# random_letter = str(input("Nhap 1 ky tu de chung toi kiem tra xem co thuoc chuoi hay khong:"))
# if random_letter in my_List:
#     print("Co ban ei")
# else:
#     print("khong co ban ei")

''' find a random string in string '''
# random_string = str(input("Nhap 1 chuoi de chung toi kiem tra xem co thuoc chuoi hay khong:"))
# if random_string in my_List:
#     print("Co ban ei")
# else:
#     print("khong co ban ei")


'''count_all_words'''
# count_words = re.findall("\w+", my_List)
# print("Cac tu trong chuoi cua ban la {}".format(count_words))

'''remove_space_at_beginning_end'''
remove_whitespace_right = my_List.rstrip()
remove_whitespace_left = my_List.lstrip()

'''only_one_space_between_characters at the string'''
the_perfect_space = re.sub("\s\s+", " ",my_List)
print(the_perfect_space)




