inputNumber1 = int(input("Hay nhap so thu nhat: "))
inputNumber2 = int(input("Hay nhap so thu hai: "))

if inputNumber1 > inputNumber2:
    highernumber = inputNumber1
    lowernumber = inputNumber2
else:
    highernumber = inputNumber2
    lowernumber = inputNumber1

for i in range(highernumber):
    i2 = i + 1
    if lowernumber * i2 == highernumber * i2 :

        print lowernumber * i2



