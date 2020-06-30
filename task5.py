proc = float(input("Введите размер выручки:"))
prod_costs = float(input("Введите размер издержек:"))
benefit = proc - prod_costs

if benefit > 0:
    count_empl = int(input("Введите количество сотрудников в компании:"))
    profit = benefit / proc
    pay = benefit / count_empl
    print(f"В вашей компании зафиксирована прибыль в размере {benefit:.2f}$\nРентабельность составила {profit}")
    print(f"Прибыль компании в расчете на одного сотрудника составляет: {pay:.2f}$")
elif benefit < 0:
    print(f"В вашей компании зафиксирован убыток в размере {benefit * -1:.2f}$")
else:
    print("Прибыль компании равна 0")