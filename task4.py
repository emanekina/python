def my_func(x, y):
    pow_calc = 1
    for i in list(range(abs(y))):
        pow_calc = pow_calc * x
    return 1 / pow_calc

print('Программа для возведения числа в отрицательную степень.')
while True:
    try:
        base = float(input(f'\nУкажите основание степени (действительное положительное число): '))
        if base <= 0:
            print('В качестве основания следует указать положительное число.')
            continue
        exponent = int(input(f'\nУкажите степень (целое отрицательное число): '))
        if exponent >= 0:
            print(f'Это программа возведения в отрицательную степень.\nБудьте внимательны.')
            continue
        print(my_func(base, exponent))
        break
    except ValueError:
        print('Упс. Что-то пошло не так.Давайте попробуем еще раз.')
        continue

