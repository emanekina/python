from itertools import count, cycle

try:
    my_list = []
    num = int(input('Введите целое число: '))
    while num <= 10:
        my_list.append(num)
        num += 1
    print(f'Результат работы итератора, генерирующего целые числа:\n{my_list}')
    print('Результат работы итератора, повторяющего элементы списка, сгенерированного выше: ')
    iter = cycle(my_list)
    for i in range(1, 11):
        print(next(iter))
except ValueError:
    print('Вы ввели некорректное значение. Программа завершена.')
