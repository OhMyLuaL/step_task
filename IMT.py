#IMT 

from re import I


weight = float(input('Введите массу '))
height = float(input('Введите рост '))

IMT = weight / height * height

if IMT > 18.5 and  IMT < 25:
    print('Оптимальная масса')
if IMT < 18.5:
    print('Недостаточная масса')
if IMT > 25:
    print('Избыточная масса')
