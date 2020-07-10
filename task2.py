from random import randint

# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [randint(0, 300) for i in range(10)]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(f'исходный список - {my_list}\nновый список - {new_list}')
