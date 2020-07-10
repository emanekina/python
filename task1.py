from sys import argv


def func_salary(work_time, rate, bonus):
    salary = work_time * rate + bonus
    return round(salary, 2)


print(argv)
try:
    uwork_time, urate, ubonus = argv[1:]
    print(f'Выработка сотрудника в часах: {uwork_time}\nПочасовая ставка сотрудника: {urate}\n'
          f'Размер премии: {ubonus}\n'
          f'Заработная плата составит: {func_salary(int(uwork_time), float(urate), float(ubonus))}')
except (ValueError, TypeError) as err:
    print('Error!', err)
