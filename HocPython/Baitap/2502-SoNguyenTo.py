# BT uoc chung lon nhat

# inputNumber1 = int(input("Hay nhap so thu nhat: "))
# inputNumber2 = int(input("Hay nhap so thu hai: "))
#
# if inputNumber1 > inputNumber2:
#     higherNumber = inputNumber1
#     lowerNumber = inputNumber2
# else:
#     higherNumber = inputNumber2
#     lowerNumber = inputNumber1
#
# result = 1
# for i in range(lowerNumber):
#     nextIndex = i + 1
#     if lowerNumber % nextIndex == 0 and higherNumber % nextIndex == 0:
#         result = nextIndex
#         print ("uoc chung", nextIndex)
#
# print ("Uoc chung lon nhat la", result)


# BT boi chung nho nhat
# inputNumber1 = int(input("Hay nhap so thu nhat: "))
# inputNumber2 = int(input("Hay nhap so thu hai: "))
#
# if inputNumber1 > inputNumber2:
#      higherNumber = inputNumber1
#      lowerNumber = inputNumber2
# else:
#      higherNumber = inputNumber2
#      lowerNumber = inputNumber1
#
# resutl = 1
# maxNumber = lowerNumber * higherNumber
# for i in range(higherNumber, maxNumber):
#     if i % higherNumber == 0 and i % lowerNumber == 0:
#         print ("Boi chung nho nhat la:", i)
#         break

# DaysoFibonacci
# inputNumber = int(input("Hay nhap vi tri so Fibonacci ma ban muon: "))

# f1 = 0
# f2 = 1
# if inputNumber == 1:
#     result = f1
# elif inputNumber == 2:
#     result = f2
# elif inputNumber > 2:
#      for i in range(2,inputNumber):
#         result = f1 + f2
#         f1 = f2
#         f2 = result
#
# print ("So Fibonacci vi tri thu {} la {}".format(inputNumber,result))

# BT so nguyen to
inputNumber = int(input("Hay nhap 1 so ma ban muon:"))

songuyento= True
for index in range(inputNumber):
    if index > 1:
        result = inputNumber % index
        if result == 0:
            songuyento = False
if songuyento:
    print ("{} la so nguyen to".format(inputNumber))
else:
    print ("{} khong phai la so nguyen to".format(inputNumber))

# BT nhap so N in ra cac so ngueyn to nho hon bang N
# inputNumber = int(input("Hay nhap 1 so ma ban muon:"))
#
# for index in range(inputNumber):
#
#     for indie in range(index):
#         songuyento = True
#         if indie > 1:
#             result = index % indie
#             if result == 0:
#                 songuyento = False
#         if songuyento:
#             print (index, indie)



