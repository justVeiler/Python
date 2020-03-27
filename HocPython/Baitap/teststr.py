# inputString = str(input("Hay nhap chuoi ky tu ma ban thich: "))
# result = inputString.replace("abc", "def")
# print(result)

# inputString = str(input("Hay nhap chuoi ky tu ma ban thich: "))
# result = inputString.replace(" ", "\n")
# print (result)

# result = inputString.split(" ")
# print(result)

# test = ["1", "2", "3", "4"]
# result = ","
# print(result.join(test))


import re


txt = "Chia sẻ tại buổi làm việc của đoàn công tác Bộ Y tế với Bệnh viện Bệnh Nhiệt đới Trung ương chiều 24/3, PGS.TS Phạm Ngọc Thạch, Giám đốc Bệnh viện Bệnh Nhiệt đới Trung ương cho biết thời gian qua số lượng bệnh nhân Covid-19 đến bệnh viện đông hơn, đa dạng về độ tuổi. Nếu như giai đoạn 1 chủ yếu là người trẻ thì giai đoạn 2 có cả tuổi cao, bệnh nền (tăng huyết áp, đái tháo đường, suy giảm miễn dịch, COPD) giống như nhiều nước hiện nay. Vì thế, diễn biến dịch của đợt này có khó khăn hơn so với trước."
# result = re.findall("[0-9]+", txt)
result = re.split("[\d]+", txt)
print(result)
