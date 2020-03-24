import sys


def print_menu():
    print("Nhap 1 de tim so nguyen to")
    print("Nhap 2 de tinh tong")
    print("Nhap 3 de tinh giai thua")
    print("Nhap 4 de exit")


def check_primary_number(check_number):
    is_primary = True
    for index in range(check_number):
        if index > 1:
            mod_result = check_number % index
            if mod_result == 0:
                is_primary = False
    if is_primary:
        print("so {} la so nguyen to".format(check_number))
    else:
        print("so {} ko phai la so nguyen to".format(check_number))


def summary(summary_input_number):
    result = 0
    for index in range(summary_input_number + 1):
        result = result + index
    print("Tong la tu 1 den {} la {}".format(summary_input_number, result))


def exponent(exponent_input_number):
    result = 1
    for index in range(2, input_number_3 + 1):
        result = result * index
    print("Tich giai thua cua {} la {}".format(exponent_input_number, result))


input_number = 0

while input_number > 4 or input_number <= 0:
    print_menu()
    input_number = int(input("Hay nhap mot so ma ban muon: "))

if input_number == 1:
    inputNumber1 = int(input("Hay nhap 1 so de chung toi kiem tra :"))
    check_primary_number(inputNumber1)

elif input_number == 2:
    input_number_2 = int(input("Hay nhap 1 so de chung toi tinh tong :"))
    summary(input_number_2)

elif input_number == 3:
    input_number_3 = int(input("Hay nhap 1 so de chung toi tinh giai thua :"))
    exponent(input_number_3)


elif input_number == 4:
    print("Da thoat he thong, xin cam on!")
    sys.exit()


