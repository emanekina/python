# создание списка
my_list = [20, 33.3, 'Hello', None, True, [1.5, 4], ('home', 1, False), {12, (1, 2)}, {1: 3, 2: 'test'}]
# определение типов элементов списка
print(my_list)
for ind, el in enumerate(my_list, 1):
    print(f"Тип {ind}-го элемента списка ({el}) - {type(el)}")
