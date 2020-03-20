print ('Nhap vao 1 so bieu thi nhiet do')
inputTemperature = input ()
isHigherThan35 = inputTemperature > 35
isLowerThan0 = 0 <= inputTemperature < 15
isMiddleLevel = 15 <= inputTemperature <= 35
isLowerThanZero = inputTemperature < 0
if isHigherThan35:
    print ('nong qua')
elif isLowerThan0:
    print ('lanh qua')
elif isMiddleLevel:
    print ('binh thuong')
else:
    print ('Nhiet do am. Vui long nhap lai')