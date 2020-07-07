def my_func(my_list):
    sum_list = 0
    for el in my_list:
        try:
            sum_list = sum_list + float(el)
        except ValueError:
            if el == '*':
                return sum_list, False
            else:
                pass
    return sum_list, True


print(f'Программа подсчитывает сумму введенных пользователем чисел.\nДля завершения программы и выхода из нее нужно ввести символ * и нажать Enter.')
total_sum = 0
pointer = True
while pointer:
    num_list = input('Укажите последовательность чисел через пробел').split()
    result_tuple = my_func(num_list)
    total_sum = total_sum + result_tuple[0]
    pointer = result_tuple[1]
    print(f'{num_list}\nСумма чисел в введенной строке: {result_tuple[0]}\nСумма всех введенных чисел: {total_sum}')
print('Программа завершена')