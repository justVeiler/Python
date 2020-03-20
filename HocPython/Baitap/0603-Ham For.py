import sys

# BT Nhap so N. Tinh tong tu 1! den N!
# inputNumber = int(input("Hay nhap so ma ban thich:"))
#
# result = 1
# result1 = 0
# for i in range(2,inputNumber + 1):
#     result = result * i
#     result1 = result1 + result
#     print ("Giai thua cua so {} la {}".format(i,result))
#     print ("Tong giai thua tu 1 den {} la {}".format(inputNumber,result1))

# BT Nhap so N. In ra so * tu 1 den N
# inputNumber = int(input("Hay nhap so ma ban thich:"))
# result = ""

# for i in range(0,inputNumber):
#     i = "*"
#     result = str(result) + i
#     print result

# BT 123*** :v
# inputNumber = int(input("Hay nhap so ma ban thich:"))

# for i in range(inputNumber+1):
#     for j in range(inputNumber+1):
#         if i < j:
#             sys.stdout.write(str(j))
#         else:
#             sys.stdout.write("*")

# print("")

# BT in tam giac can

# inputNumber = int(input("Hay nhap so ma ban thich:"))
#
# matrixWidth = inputNumber * 2
#
# matrixHeight = int(round(matrixWidth / 2))
#
# for i in range(0, matrixHeight):
#     for j in range(0, matrixWidth):
#         if j < matrixWidth * 0.5 - i or j > matrixWidth * 0.5 + i:
#             sys.stdout.write(" ")
#         else:
#             sys.stdout.write("*")
#     print("")



# BT Giai PT bac 2
# import math
#
#
# class float:
#
#     inputNumber1 = int(input("Hay nhap so A:"))
#     inputNumber2 = int(input("Hay nhap so B:"))
#     inputNumber3 = int(input("Hay nhap so B:"))
#     if inputNumber1 == 0:
#         print ("Nhap lai di, A phai khac 0")
#
#     delta = (inputNumber2 * inputNumber2) - (4 * inputNumber1 * inputNumber3)
#     print ("Delta = ", delta)
#     if delta < 0:
#         print ("Phuong trinh vo nghiem.")
#     elif delta == 0:
#         a = (- inputNumber2) / (2 * inputNumber1)
#         print ("Phuong trinh co nghiem kep la {}").format(a)
#     elif delta > 0:
#         a = ((- inputNumber2) + math.sqrt(delta)) / (2 * inputNumber1)
#         b = ((- inputNumber2) - math.sqrt(delta)) / (2 * inputNumber1)
#         print ("Phuong trinh co 2 nghiem la {} va {}").format(a,b)
#
