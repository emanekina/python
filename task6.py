result_1 = float(input("Сколько километров ты пробежал сегодня?"))
goal = float(input("Введи цель. Сколько километров в день ты хочешь пробегать?"))
num_day = 1
print(f"Результаты:\n{num_day}-й день - {result_1:.2f} км")
while result_1 < goal:
    result_1 = result_1 + result_1 * 0.1
    num_day += 1
    print(f"{num_day}-й день - {result_1:.2f} км")
print(f"На {num_day}-й день ты достигнешь желаемого результата - не менее {goal:.2f} км")