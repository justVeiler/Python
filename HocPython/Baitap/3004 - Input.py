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


inputName = ""
inputAge = ""

listLength = 3

listAges = [0] * listLength
listNames = [''] * listLength

for i in range(listLength):
    inputName1 = str(input("Hay nhap ten nguoi thu {}: ".format(i + 1)))
    inputAge1 = int(input("Hay nhap ten nguoi do: "))
    listAges[i] = inputAge1
    listNames[i] = inputName1

theOldest = max(listAges)
position = listAges.index(max(listAges))
print(position)
