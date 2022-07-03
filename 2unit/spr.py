def game():
    Timur_string = input()
    Ruslan_string = input()

    if Timur_string == 'камень' and Ruslan_string == 'ножницы':
        print('Тимур')
    elif Timur_string == 'ножницы' and Ruslan_string == 'бумага':
        print('Тимур')
    elif Timur_string == 'бумага' and Ruslan_string == 'камень':
        print('Тимур')
    elif Timur_string == Ruslan_string:
        print('ничья')
    else:
        print('Руслан')

game()