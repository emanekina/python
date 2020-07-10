from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield i, factorial(i)


try:
    num = int(input('Введите число: '))
    for i, el in fact(num):
        print(f'{i}! = {el}')
except ValueError:
    print('Вы ввели не число. Программа завершена.')

