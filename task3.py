def my_func(a1, a2, a3):
    elements = [a1, a2, a3]
    elements.remove(min(elements))
    return sum(elements)


while True:
    try:
        num_1 = int(input(f'Введите первое число: '))
        num_2 = int(input(f'Введите второе число: '))
        num_3 = int(input(f'Введите третье число: '))
        print('Сумма двух наибольших из введенных чисел = ', my_func(num_1, num_2, num_3))
        break
    except ValueError:
        print('Введенное значение не является целым числом. Повторите ввод чисел.')
        continue
