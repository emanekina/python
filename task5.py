total_sum = 0
print(f'Программа подсчитывает сумму введенных пользователем чисел.\nДля завершения программы и выхода из нее нужно ввести символ * и нажать Enter.')
while True:
    num_list = input('Укажите последовательность чисел через пробел').split()
    print(num_list)
    for el in num_list:
        try:
            total_sum = total_sum + float(el)
        except ValueError:
            print('Сумма всех введенных пользователем чисел равна ', total_sum)
            print('Выполнение программы завершено')
            break
    print('Сумма введенных пользователем чисел равна ', total_sum)
    continue

