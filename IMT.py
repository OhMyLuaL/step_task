#IMT 

from re import I


weight = float(input('Введите массу '))
height = float(input('Введите рост '))

imt = (weight / height ** 2)

if imt >= 18.5 or imt <= 25:
    print('Оптимальная масса')

if imt < 18.5:
    print('Недостаточная масса')

if imt > 25:
    print('Избыточная масса')