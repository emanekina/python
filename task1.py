def division_func(var_1, var_2):
    try:
        var_3 = var_1 / var_2
        return var_3
    except ZeroDivisionError:
        print('Деление на ноль не допускается!')


print('Функция вычисляет частное двух чисел.')
while True:
    try:
        div_1 = int(input(f'Введите первое число: '))
        div_2 = int(input(f'Введите второе число: '))
        print(division_func(div_1, div_2))
        break
    except ValueError:
        print('Введено неверное значение параметра. Попробуйте ввести числа еще раз.')
        continue
